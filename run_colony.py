"""
==========================================
run_colony.py — Colony MAS Entry Point
==========================================
"""

from colony.core.engine import ColonyEngine
from colony.agents.base_agent import BaseAgent


class SimpleAgent(BaseAgent):
    def perceive(self):
        print(f"[{self.name}] perceiving...")

    def decide(self):
        return "process_data"

    def act(self, action):
        super().act(action)


if __name__ == "__main__":
    engine = ColonyEngine()

    agent1 = SimpleAgent("Agent-1")
    agent2 = SimpleAgent("Agent-2")

    engine.register_agent(agent1)
    engine.register_agent(agent2)

    engine.run(steps=5)
