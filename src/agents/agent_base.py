from abc import ABC, abstractmethod


class AgentBase:
    def __init__(self, name, description, tools, model, authorizations, memory):
        self.name = name
        self.description = description
        self.tools = tools
        self.model = model
        self.authorizations = authorizations
        self.memory = memory
        self.state = state

    @abstractmethod
    def analyze(self, data):
        pass

    @abstractmethod
    def plan(self, objective):
        pass

    @abstractmethod
    def validate(self, objective):
        pass

    @abstractmethod
    def execute(self, plan):
        pass
