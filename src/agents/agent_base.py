from abc import ABC, abstractmethod


class AgentBase:
    def __init__(self, name, description, tools, model, authorizations, state, memory):
        self.name = name
        self.description = description
        self.tools = tools
        self.model = model
        self.authorizations = authorizations
        self.state = state
        self.memory = memory

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


class CustomerServiceAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Customer Service Agent",
            description="This agent is designed to assist customers by answering their questions and providing support.",
            tools=["ConversationTool"],
            model="gpt-4o-mini",
            authorizations=[],
            state="created",
            memory={},
        )


class TechnicalSupportAgent(AgentBase):
    def __init__(self):
        super().__init__(
            name="Technical Support Agent",
            description="This agent specializes in troubleshooting technical issues and providing solutions.",
            tools=["ContextRetrievalTool"],
            model="gpt-4o-mini",
            authorizations=["auth2"],
            state="created",
            memory={},
        )
