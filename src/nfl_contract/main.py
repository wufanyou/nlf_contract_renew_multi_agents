#!/usr/bin/env python
import warnings

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
import os

from nfl_contract.crew import NflContract
import pandas as pd
import xmltodict

PLAYER_ID = int(os.getenv("PLAYER_ID")) # type: ignore
INPUT_DATA = "./knowledge/agent_input/{player_name}.xml"
DATA = "./knowledge/contract_details.csv"


def prepare_inputs(player_id: int):

    df = pd.read_csv(DATA)
    row = df.iloc[player_id]
    player_name = row["player"].lower().replace(" ", "_")
    with open(f"./knowledge/agent_input/{player_name}.xml", "r") as f:
        input_data = xmltodict.parse(f.read())
    output = {}

    def f(k: str, v: dict | str):
        if isinstance(v, dict):
            for k1, v1 in v.items():
                f(k1, v1)
        else:
            output[k] = v

    for k, v in input_data.items():
        f(k, v)

    return output


def run():

    try:
        NflContract().crew().kickoff(
            inputs=prepare_inputs(PLAYER_ID)
        )
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
