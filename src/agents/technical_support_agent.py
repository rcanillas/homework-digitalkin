from agents.agent_base import BaseAgent


class TechnicalSupportAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Technical Support Agent",
            purpose="An AI Agent that specialized in retrieving technical issue in documents.",
            tools=["Context Retrieval Tool"],
            model="gpt-4o-mini",
            authorizations=[],
        )
