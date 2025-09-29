import re
import time

import anthropic
import pandas as pd
from anthropic.types import TextBlock
from tqdm import tqdm

client = anthropic.Anthropic()

XML_TEMPLATE = """
<output>
    <player_information>
        <position>Quarterback</position>
        <player_name>Marcus Williams</player_name>
        <years_experience>6</years_experience>
        <key_achievements>Pro Bowl selections in 2022 and 2023, led team to playoff appearances, 4,200+ passing yards per season</key_achievements>
        <performance_goals>leading the team to a Super Bowl championship and maintaining elite quarterback statistics</performance_goals>
    </player_information>
    
    <team_information>
        <team_name>Denver Broncos</team_name>
        <division>AFC West</division>
        <team_strategy>building a championship-caliber team around a strong offensive core</team_strategy>
        <team_success>two playoff appearances and one division title</team_success>
        <salary_cap_space>$45 million</salary_cap_space>
    </team_information>
    
    <contract_financial_details>
        <contract_years>4</contract_years>
        <analysis_period>3</analysis_period>
        <performance_metrics>passing yards, touchdown-to-interception ratio, team wins, and playoff performance</performance_metrics>
    </contract_financial_details>
    
    <agent_information>
        <agent_experience>12</agent_experience>
        <total_contracts_value>500</total_contracts_value>
    </agent_information>
    
    <family_information>
        <dependents_count>3</dependents_count>
        <family_priorities>children's education and long-term financial security</family_priorities>
        <children_education>private school tuition and college funds</children_education>
    </family_information>
    
    <coaching_management>
        <coaching_experience>8</coaching_experience>
        <player_coach_relationship>3 years</player_coach_relationship>
        <gm_experience>10</gm_experience>
    </coaching_management>
    
    <ownership_information>
        <ownership_experience>15</ownership_experience>
        <franchise_value>4.2</franchise_value>
        <championship_success>one Super Bowl appearance and multiple playoff runs</championship_success>
        <business_priorities>revenue growth and fan engagement</business_priorities>
    </ownership_information>
</output>"""


def get_output(player: str):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""Search from the information from the web and extract the relevant information about the NFL player ({player}). 
                Make sure to fill in all fields with accurate data.\n"""
                + XML_TEMPLATE,
            }
        ],
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 10}],
    )
    text = "\n".join([k.text for k in response.content if isinstance(k, TextBlock)])
    return text


def extract_xml_text(xml_string: str, tag_name: str):
    pattern = rf"<{tag_name}[^>]*>(.*?)</{tag_name}>"
    matches = re.findall(pattern, xml_string, re.DOTALL)
    return [match.strip() for match in matches]


if __name__ == "__main__":
    data = pd.read_csv("./knowledge/contract_details.csv")
    data = data[4:]
    
    for index, row in tqdm(data.iterrows(), total=data.shape[0]):
        while True:
            try:
                player = row["player"] + " " + row["pos"] + " " + row["team_currently_with"]
                output = get_output(player)
                extracted_data = extract_xml_text(output, "output")
                if extracted_data:
                    extracted_data = extracted_data[0]
                    with open(
                        f"./knowledge/agent_input/{row['player'].lower().replace(' ', '_')}.xml",
                        "w",
                    ) as f:
                        extracted_data = "<output>\n" + extracted_data + "\n</output>"
                        f.write(extracted_data)
                break
            except Exception as e:
                print(f"Error occurred: {e}. Retrying in 60 seconds...")
                time.sleep(60)
        time.sleep(60)
