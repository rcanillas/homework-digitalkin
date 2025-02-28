import pytest
from agents.tools import ConversationTool, ContextRetrievalTool


@pytest.fixture
def conversation_tool():
    return ConversationTool()


@pytest.fixture
def context_retrieval_tool():
    return ContextRetrievalTool()


def test_execute_conversation_tool(conversation_tool, monkeypatch):
    context = "This is a test context. The purpose of this test is to answer '42'."
    question = "What is the purpose of this test?"
    parameters = {"context": context, "message": question}
    response = conversation_tool.execute_task(None, parameters)
    assert isinstance(response, str)
    assert len(response) > 0
    assert response == "The purpose of this test is to answer '42'."


def test_execute_context_retrieval_tool(context_retrieval_tool, monkeypatch):
    text = "Computer won't turn on"
    expected_context = "Issue: Computer won't turn on\n,Steps: Check if the power cable is properly connected to the computer and the power outlet.\n  Ensure the power outlet is working by testing another device.\n  Press the power button firmly for at least 5 seconds.\n  If the computer still doesn't turn on, try using a different power cable.\n  Inspect the power supply unit for any visible damage or loose connections.\n  If all else fails, consult a professional technician."
    parameters = {"text": text}
    response = context_retrieval_tool.execute_task(None, parameters)
    assert isinstance(response, str)
    assert len(response) > 0
    assert response == expected_context
