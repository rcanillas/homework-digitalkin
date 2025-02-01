class ConversationTool:
    def __init__(self, name, purpose, parameters, exec_function):
        self.name = name
        self.purpose = purpose
        self.parameters = parameters
        self.exec_function = exec_function

    def execute(self, context, question):
        # Simulate using an LLM to generate an answer
        return f"Answer to '{question}' based on context '{context}'"

class ContextRetrievalTool:
    def __init__(self, name, purpose, parameters, exec_function):
        self.name = name
        self.purpose = purpose
        self.parameters = parameters
        self.exec_function = exec_function

    def execute(self, text, documents):
        # Simulate finding the most relevant document
        return f"Most relevant document for '{text}'"
