from agents.base_agent import BaseAgent
from agents.tools import ConversationTool


conversationTool = ConversationTool()


class CustomerServiceAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Customer Service Agent",
            purpose="A customer service agent that use the conversation tool to give answers to basic queries from the user."
            "You always check first if you can use other agents or tools to gather context about the question."
            "Then you answer the question as best you can. You must always answer the question.",
            tools=[conversationTool],
            signature={"message": "str"},
            model="gpt-4o-mini",
            authorizations=[],
        )
