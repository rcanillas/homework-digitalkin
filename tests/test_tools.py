import pytest
from agents.tools import ConversationTool

@pytest.fixture
def conversation_tool():
    return ConversationTool(
        name="Test Conversation Tool",
        purpose="Test purpose",
        parameters={},
        exec_function=None
    )

def test_execute(conversation_tool):
    context = "This is a test context."
    question = "What is the purpose of this test?"
    response = conversation_tool.execute(context, question)
    assert isinstance(response, str)
    assert len(response) > 0
