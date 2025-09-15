from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class NflContract():
    """NflContract crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def nfl_player(self) -> Agent:
        return Agent(
            config=self.agents_config['nfl_player'],  # type: ignore[index]
            verbose=True
        ) 

    @agent
    def player_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['player_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def player_family(self) -> Agent:
        return Agent(
            config=self.agents_config['player_family'], # type: ignore[index]
            verbose=True
        )

    @agent
    def head_coach(self) -> Agent:
        return Agent(
            config=self.agents_config['head_coach'], # type: ignore[index]
            verbose=True
        )

    @agent
    def team_owner(self) -> Agent:
        return Agent(
            config=self.agents_config['team_owner'], # type: ignore[index]
            verbose=True
        )

    @agent
    def general_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['general_manager'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def player_performance_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['player_performance_analysis'], # type: ignore[index]
        )

    @task
    def salary_cap_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['salary_cap_analysis'], # type: ignore[index]
        )

    @task
    def contract_terms_negotiation(self) -> Task:
        return Task(
            config=self.tasks_config['contract_terms_negotiation'], # type: ignore[index]
        )

    @task
    def family_financial_planning(self) -> Task:
        return Task(
            config=self.tasks_config['family_financial_planning'], # type: ignore[index]
        )

    @task
    def roster_construction_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['roster_construction_analysis'], # type: ignore[index]
        )

    @task
    def coaching_evaluation(self) -> Task:
        return Task(
            config=self.tasks_config['coaching_evaluation'], # type: ignore[index]
        )

    @task
    def business_impact_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['business_impact_analysis'], # type: ignore[index]
        )

    @task
    def risk_assessment_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['risk_assessment_analysis'], # type: ignore[index]
        )

    @task
    def market_leverage_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['market_leverage_analysis'], # type: ignore[index]
        )

    @task
    def contract_recommendation(self) -> Task:
        return Task(
            config=self.tasks_config['contract_recommendation'], # type: ignore[index]
            output_file='contract_recommendation.md'
        )

    @task
    def media_strategy_planning(self) -> Task:
        return Task(
            config=self.tasks_config['media_strategy_planning'], # type: ignore[index]
            output_file='media_strategy.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the NflContract crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
