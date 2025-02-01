import openai

class ConversationTool:
    def __init__(self, name, purpose, parameters, exec_function):
        self.name = name
        self.purpose = purpose
        self.parameters = parameters
        self.exec_function = exec_function

    def execute(self, context, question):
        # Call OpenAI API to generate an answer
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": question}
            ],
            max_tokens=150
        )
        return response.choices[0].text.strip()

class ContextRetrievalTool:
    def __init__(self, name, purpose, parameters, exec_function):
        self.name = name
        self.purpose = purpose
        self.parameters = parameters
        self.exec_function = exec_function

    def execute(self, text, documents):
        # Simulate finding the most relevant document
        return f"Most relevant document for '{text}'"
