from agents.agent_factory import Agent

CustomerServiceAgent = Agent(
    name="Customer Service Agent",
    description="First AI agent",
    tools=["tool1", "tool2"],
    model="model1",
    authorizations=["auth1"],
    memory={}
)
