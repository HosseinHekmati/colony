from colony.core.container import Container
from colony.core.scheduler import select_agents

from colony.agents.local_agent import LocalAgent
from colony.agents.online_agent import OnlineAgent
from colony.agents.rag_agent import RAGAgent

from colony.utils.logger import log


def run_colony():
    log("Initializing Colony...")

    container = Container()

    # Register agents
    agents = [
        LocalAgent(),
        OnlineAgent(),
        RAGAgent()
    ]

    for agent in agents:
        container.register(agent)

    log("Agents registered.")

    while True:
        user_input = input("\n[User] > ")

        if user_input.lower() in ["exit", "quit"]:
            log("Shutting down Colony.")
            break

        selected_agents = select_agents(user_input, container.get_agents())

        for agent in selected_agents:
            response = agent.run(user_input)
            print(f"[{agent.name}] {response}")
