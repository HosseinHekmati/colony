class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.engine = None

    def attach_system(self, engine):
        self.engine = engine

    def perceive(self):
        """Read from memory or environment"""
        pass

    def decide(self):
        """Return an action"""
        return "idle"

    def act(self, action):
        print(f"[Agent:{self.name}] Action -> {action}")
