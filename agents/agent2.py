from agents.agent_factory import Agent

TechnicalSupportAgent = Agent(
    name="Technical Support Agent",
    description="Second AI agent",
    tools=["tool3", "tool4"],
    model="model2",
    authorizations=["auth2"],
    memory={}
)
