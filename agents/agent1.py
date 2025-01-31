class Agent:
    def __init__(self, name):
        self.name = name

    def respond(self, message):
        return f"{self.name} received: {message}"

agent1 = Agent("Agent 1")
