from agents.agent_base import AgentBase

TechnicalSupportAgent = AgentBase(
    name="Technical Support Agent",
    description="Second AI agent",
    tools=["tool3", "tool4"],
    model="model2",
    authorizations=["auth2"],
    state="created",
    memory={},
)
