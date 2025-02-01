import pytest
from agents.customer_service_agent import CustomerServiceAgent
from agents.technical_support_agent import TechnicalSupportAgent

@pytest.fixture
def cs_agent():
    return CustomerServiceAgent()

@pytest.fixture
def ts_agent():
    return TechnicalSupportAgent()

def test_CustomerServiceAgent_response(cs_agent):
    assert cs_agent.respond("Hello") == "Customer Service Agent received: Hello"

def test_TechnicalSupportAgent_response(ts_agent):
    assert ts_agent.respond("Hello") == "Technical Support Agent received: Hello"

def test_analyze_function(ts_agent):
    user_message = "I need help with my computer."
    parameters = {"urgency": "high"}
    tool_specifications = [
        {"name": "Conversation Tool", "purpose": "Answer user questions"},
        {"name": "Context Retrieval Tool", "purpose": "Retrieve relevant documents"},
    ]
    agent_memory = {"previous_tasks": []}

    best_tools = ts_agent.analyze(user_message, parameters, tool_specifications, agent_memory)
    expected_tools = ["Context Retrieval Tool"]  # Assuming this is the expected output

    assert best_tools == expected_tools
