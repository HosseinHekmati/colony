from colony.agents.manager import AgentManager
from colony.memory.memory_manager import MemoryManager
from colony.communication.bus import MessageBus


class ColonyEngine:
    def __init__(self):
        self.agent_manager = AgentManager()
        self.memory = MemoryManager()
        self.bus = MessageBus()
        self.running = False

    def register_agent(self, agent):
        self.agent_manager.add_agent(agent)
        agent.attach_system(self)

    def step(self):
        """Single execution step"""
        for agent in self.agent_manager.get_agents():
            agent.perceive()
            action = agent.decide()
            agent.act(action)

    def run(self, steps=10):
        self.running = True
        print("[Colony] Starting engine...")

        for i in range(steps):
            print(f"[Colony] Step {i+1}")
            self.step()

        print("[Colony] Execution finished.")
