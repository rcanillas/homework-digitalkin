from agents.agent_base import AgentBase

CustomerServiceAgent = AgentBase(
    name="Customer Service Agent",
    description="First AI agent",
    tools=["tool1", "tool2"],
    model="model1",
    authorizations=[],
    state="created",
    memory={},
)
