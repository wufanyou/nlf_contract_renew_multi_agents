#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from nfl_contract.crew import NflContract

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        # Player Information
        'position': 'Quarterback',
        'player_name': 'Marcus Williams',
        'years_experience': 6,
        'key_achievements': 'Pro Bowl selections in 2022 and 2023, led team to playoff appearances, 4,200+ passing yards per season',
        'performance_goals': 'leading the team to a Super Bowl championship and maintaining elite quarterback statistics',
        
        # Team Information
        'team_name': 'Denver Broncos',
        'division': 'AFC West',
        'team_strategy': 'building a championship-caliber team around a strong offensive core',
        'team_success': 'two playoff appearances and one division title',
        'salary_cap_space': '$45 million',
        
        # Contract & Financial Details
        'contract_years': 4,
        'analysis_period': 3,
        'performance_metrics': 'passing yards, touchdown-to-interception ratio, team wins, and playoff performance',
        
        # Agent Information
        'agent_experience': 12,
        'total_contracts_value': 500,
        
        # Family Information
        'dependents_count': 3,
        'family_priorities': 'children\'s education and long-term financial security',
        'children_education': 'private school tuition and college funds',
        
        # Coaching & Management
        'coaching_experience': 8,
        'player_coach_relationship': '3 years',
        'gm_experience': 10,
        
        # Ownership Information
        'ownership_experience': 15,
        'franchise_value': 4.2,
        'championship_success': 'one Super Bowl appearance and multiple playoff runs',
        'business_priorities': 'revenue growth and fan engagement',
        
        # Current Year
        'current_year': str(datetime.now().year)
    }
    
    try:
        NflContract().crew(output_log_file=True).kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        NflContract().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        NflContract().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        NflContract().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
