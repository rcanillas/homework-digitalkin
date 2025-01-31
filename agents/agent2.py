class Agent:
    def __init__(self, name):
        self.name = name

    def respond(self, message):
        return f"{self.name} received: {message}"

agent2 = Agent("Agent 2")
