import pytest
from agents.base_agent import BaseAgent
from agents.tools import DummyTool


@pytest.fixture
def dummy_tool():
    return DummyTool(name="Dummy Tool")


@pytest.fixture
def dummy_agent(dummy_tool):
    return BaseAgent(
        name="Dummy Agent",
        purpose="A dummy agent for testing purposes",
        tools=[dummy_tool],
        model="gpt-4o-mini",
        authorizations=[],
        signature={},
    )


def test_analyze_function(dummy_agent):
    user_message = "I need to test my agent."
    parameters = {"answer": None}
    retrieved_tools = dummy_agent.analyze(
        user_message,
        parameters,
    )
    expected_tools = {"tools": ["Dummy Tool"]}  # Assuming this is the expected output

    assert retrieved_tools == expected_tools


def test_plan_function(dummy_agent):
    user_message = "I need to test my agent. The test must give me the correct answer."
    parameters = {"answer": 42}
    selected_tools = {"tools": ["Dummy Tool"]}  # Assuming this is the expected output
    expected_steps = [
        {
            "tool": "Dummy Tool",
            "parameters": {"answer": 42},
            "task": "Test the agent by providing the correct answer.",
        }
    ]
    retrieved_steps = dummy_agent.plan(user_message, parameters, selected_tools)
    print(retrieved_steps)
    assert retrieved_steps[0]["tool"] == expected_steps[0]["tool"]
    assert retrieved_steps[0]["parameters"] == expected_steps[0]["parameters"]


def test_execute_function(dummy_agent):
    user_message = "I need to test my agent. The test must give me the correct answer."
    parameters = {"answer": 42}
    plan = [
        {
            "tool": "Dummy Tool",
            "parameters": {"answer": 42},
            "task": "test the execute function",
        }
    ]
    expected_result = [f"Test completed. The parameters is {parameters['answer']}"]
    retrieved_result = dummy_agent.execute(plan)
    assert retrieved_result == expected_result


# Formulation can change, this needs to be fixed
def test_validate_function(dummy_agent):
    user_message = "I need to test my agent. The test must give me the correct answer."
    parameters = {"answer": 42}
    plan = [{"tool": "Dummy Tool", "parameters": {"answer": 42}}]
    result = [f"Test completed. The parameters is {parameters['answer']}"]
    retrieved_validation = dummy_agent.validate(user_message, parameters, plan, result)
    print(retrieved_validation)
    expected_validation = {
        "is_valid": True,
        "validity_reason": "The plan was executed correctly as the agent's result confirms that the test was completed with the expected answer of 42.",
    }
    # Skipping exact formulation for now
    assert retrieved_validation["is_valid"] == expected_validation["is_valid"]


def test_execute_task(dummy_agent):
    task_data = {
        "task": "I need to test my agent. The test must give me the correct answer.",
        "parameters": {"answer": 42},
    }
    retrieved_result = dummy_agent.execute_task(
        task_data["task"], task_data["parameters"]
    )
    expected_result = {
        "result": [
            f"Test completed. The parameters is {task_data["parameters"]['answer']}"
        ],
        "validity": {
            "is_valid": True,
            "validity_reason": "The plan was executed correctly as the agent's result confirms that the test was completed with the expected answer of 42.",
        },
    }
