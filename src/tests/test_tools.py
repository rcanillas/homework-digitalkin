import pytest
from agents.tools import ConversationTool


@pytest.fixture
def conversation_tool():
    return ConversationTool(
        name="Test Conversation Tool",
        parameters={"llm_model": "gpt-4o-mini"},
    )


def test_execute(conversation_tool, monkeypatch):
    context = "This is a test context. The purpose of this test is to answer '42'."
    question = "What is the purpose of this test?"
    response = conversation_tool.execute(context, question)
    assert isinstance(response, str)
    assert len(response) > 0
    assert response == "The purpose of this test is to answer '42'."
