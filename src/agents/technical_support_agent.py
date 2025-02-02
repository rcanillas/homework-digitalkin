from agents.base_agent import BaseAgent

# This could be done with an "init" func to register tools from external repos
from agents.tools import ContextRetrievalTool

contextRetrievalTool = ContextRetrievalTool()


class TechnicalSupportAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Technical Support Agent",
            purpose="An AI Agent that specialized in retrieving technical issue in documents.",
            tools=[contextRetrievalTool],
            model="gpt-4o-mini",
            authorizations=[],
            signature={"text": "str"},
        )
