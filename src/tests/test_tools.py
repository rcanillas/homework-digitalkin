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

def test_execute(conversation_tool, monkeypatch):
    context = "This is a test context."
    question = "What is the purpose of this test?"

    # Mock the OpenAI API call
    def mock_execute(context, question):
        return "This is a mock response."

    monkeypatch.setattr(conversation_tool, 'exec_function', mock_execute)

    response = conversation_tool.execute(context, question)
    assert isinstance(response, str)
    assert len(response) > 0
    assert response == "This is a mock response."
