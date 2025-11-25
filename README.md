# NflContract Crew

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/nfl_contract/config/agents.yaml` to define your agents
- Modify `src/nfl_contract/config/tasks.yaml` to define your tasks
- Modify `src/nfl_contract/crew.py` to add your own logic, tools and specific args
- Modify `src/nfl_contract/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ PLAYER_ID=0 uv run crewai run
```

## Understanding Your Crew

The nfl_contract Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
