from agents.base_agent import BaseAgent
from dotenv import load_dotenv

load_dotenv()

import streamlit as st

# Show title and description.
st.title("💬AI Agents demo")
st.write(
    "This is a simple test for an Agentic Mesh framework (incomplete). It aims to showcase the core concept of agents, and their interaction."
)

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management

# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.

customerServiceAgent = BaseAgent(
    name="Customer Service Agent",
    purpose="A customer service agent that use the conversation tool to give answers to basic queries from the user."
    "You always check first if you can use other agents or tools to gather context about the question."
    "Then you answer the question as best you can. You must always answer the question.",
    tools=[conversationTool],
    signature={"message": "str"},
    model="gpt-4o-mini",
    authorizations=[],
)
technicalSupportAgent = BaseAgent(
    name="Technical Support Agent",
    purpose="An AI Agent that specialized in retrieving technical issue in documents.",
    tools=[contextRetrievalTool],
    model="gpt-4o-mini",
    authorizations=[],
    signature={"text": "str"},
)
# Adding the technical support agent as a tool of the customer service agent (should be done by registering with registry)
customerServiceAgent.tools.append(technicalSupportAgent)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("What is up?"):

    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

        # Generate a response using the Customer Service Agent.
        answer = customerServiceAgent.execute_task(f"Answer this message: {prompt}", {})
        # Stream the response to the chat using `st.write_stream`, then store it in
        # session state.
    with st.chat_message("assistant"):
        response = st.markdown(answer["result"][0])
        st.session_state.messages.append({"role": "assistant", "content": response})
