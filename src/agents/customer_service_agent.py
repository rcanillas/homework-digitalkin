from agents.agent_base import BaseAgent


class CustomerServiceAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Customer Service Agent",
            purpose="A customer service agent that answer to basic queries from the user.",
            tools=["Conversation Tool"],
            model="gpt-4o-mini",
            authorizations=[],
        )
