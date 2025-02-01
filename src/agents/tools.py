from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class ConversationTool:
    def __init__(self, name, purpose, parameters, exec_function):
        self.name = name
        self.purpose = purpose
        self.parameters = parameters
        self.exec_function = exec_function

    def execute(self, context, question):
        # Call OpenAI API to generate an answer
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "developer", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Context:{context}\n" + f"Question:{question}",
                },
            ],
        )


class ContextRetrievalTool:
    def __init__(self, name, purpose, parameters, exec_function):
        self.name = name
        self.purpose = purpose
        self.parameters = parameters
        self.exec_function = exec_function

    def execute(self, text, documents):
        # Simulate finding the most relevant document
        return f"Most relevant document for '{text}'"
