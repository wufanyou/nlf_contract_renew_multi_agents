import re
import glob
import json
import pandas as pd


# for any contract_recommendation.md in output folder, extract the json part and save to evaluation folder
def extract_json_from_md(file_path: str) -> str:
    with open(file_path, "r") as f:
        content = f.read()
    match = re.search(r"```json(.*?)```", content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


if __name__ == "__main__":
    md_files = glob.glob("./output/*/contract_recommendation.md")
    md_files.sort()
    md_files = md_files[1:]

    output = []
    indexs = []
    i = 0
    for md_file in md_files:
        json_content = extract_json_from_md(md_file)

        print(json_content)
        if json_content:
            index = int(md_file.split("/")[2])
            if "moderate" in json_content:
                output.append(json.loads(json_content)['moderate'])
            else:
                output.append(json.loads(json_content))


            # convert the unit of value and signing_bonus for index 14
            if index == 14:
                output[-1]['value'] *= 1000000
                output[-1]['signing_bonus'] *= 1000000

            indexs.append(index)


    df = pd.DataFrame(output, index=indexs)
    print(df)
    df.to_csv("contract_recommendation.csv")
