import tempfile
from typing import List
import os
import pandas as pd
from crewai import Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
from crewai.project import CrewBase, agent, crew, task

CONTRACT_DATA = "./knowledge/contract_details.csv"
STAT_DATA = "./knowledge/wr_stats_for_ai_negotiator.csv"
PLAYER_ID = int(os.getenv("PLAYER_ID")) # type: ignore

def prepare_data(player_id: int) -> str:
    df = pd.read_csv(CONTRACT_DATA)
    df['contract_date'] = pd.to_datetime(df['contract_date'])
    contract_date = df.iloc[player_id]["contract_date"]
    df = df[df['contract_date'] < contract_date].reset_index(drop=True)
    df = df.sort_values(by='contract_date', ascending=False).reset_index(drop=True)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    df.to_csv(temp_file.name, index=False)
    return temp_file.name


@CrewBase
class NflContract:
    """NflContract crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def nfl_player(self) -> Agent:
        return Agent(
            config=self.agents_config["nfl_player"], verbose=True  # type: ignore[index]
        )

    @agent
    def player_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["player_agent"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def player_family(self) -> Agent:
        return Agent(
            config=self.agents_config["player_family"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def head_coach(self) -> Agent:
        return Agent(
            config=self.agents_config["head_coach"], verbose=True  # type: ignore[index]
        )

    @agent
    def team_owner(self) -> Agent:
        return Agent(
            config=self.agents_config["team_owner"], verbose=True  # type: ignore[index]
        )

    @agent
    def general_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["general_manager"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def player_performance_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["player_performance_analysis"],  # type: ignore[index]
        )

    @task
    def salary_cap_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["salary_cap_analysis"],  # type: ignore[index]
        )

    @task
    def contract_terms_negotiation(self) -> Task:
        return Task(
            config=self.tasks_config["contract_terms_negotiation"],  # type: ignore[index]
        )

    @task
    def family_financial_planning(self) -> Task:
        return Task(
            config=self.tasks_config["family_financial_planning"],  # type: ignore[index]
        )

    @task
    def roster_construction_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["roster_construction_analysis"],  # type: ignore[index]
        )

    @task
    def coaching_evaluation(self) -> Task:
        return Task(
            config=self.tasks_config["coaching_evaluation"],  # type: ignore[index]
        )

    @task
    def business_impact_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["business_impact_analysis"],  # type: ignore[index]
        )

    @task
    def risk_assessment_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["risk_assessment_analysis"],  # type: ignore[index]
        )

    @task
    def market_leverage_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["market_leverage_analysis"],  # type: ignore[index]
        )

    @task
    def contract_recommendation(self) -> Task:
        return Task(
            config=self.tasks_config["contract_recommendation"],  # type: ignore[index]
            output_file=f"./output/{PLAYER_ID}/contract_recommendation.md",
        )

    @task
    def media_strategy_planning(self) -> Task:
        return Task(
            config=self.tasks_config["media_strategy_planning"],  # type: ignore[index]
            output_file=f"./output/{PLAYER_ID}/media_strategy.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the NflContract crew"""

        knowledge_sources = [
            CSVKnowledgeSource(
                file_path=prepare_data(PLAYER_ID),
                collection_name="other_players_contracts",
            ),
            CSVKnowledgeSource(
                file_path=STAT_DATA, collection_name="wr_stats_for_recent_3_years"
            ),
        ]
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            knowledge_sources=knowledge_sources,  # type: ignore[call-arg]
        )
