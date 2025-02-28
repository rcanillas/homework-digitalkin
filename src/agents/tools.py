import json

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()

DEFAULT_LLM_MODEL = "gpt-4o-mini"
DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"


def _compute_cosine_similarity(embed_1, embed_2):
    # Calculate dot product
    dot_product = sum(a * b for a, b in zip(embed_1, embed_2))

    # Calculate the magnitude of each vector
    magnitude_A = sum(a * a for a in embed_1) ** 0.5
    magnitude_B = sum(b * b for b in embed_2) ** 0.5

    # Compute cosine similarity
    cosine_similarity = dot_product / (magnitude_A * magnitude_B)
    return cosine_similarity


class ConversationTool:
    def __init__(self):
        self.name = "Conversation Tool"
        # probably could use class attributes here
        self.purpose = "A tool that allows Agent to answer to users, using a provided context if needed."
        # probably should add some config

        # We need to add signature to tell Agent how to execute the tool
        self.signature = {"message": "str", "context": "str"}

    def execute_task(self, task, parameters):
        # Call OpenAI API to generate an answer
        parameters["context"] = (
            None if "context" not in parameters else parameters["context"]
        )
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[
                {
                    "role": "developer",
                    "content": "You are a helpful assistant. You answer the question using the context provided (if the context is provided).",
                },
                {
                    "role": "user",
                    "content": f"Context:{parameters['context']}\n"
                    + f"Question:{parameters['message']}",
                },
            ],
        )
        return completion.choices[0].message.content


class ContextRetrievalTool:
    # This tool is very specific, should be generalized
    def __init__(self):
        self.name = "Context Retrieval Tool"
        self.purpose = "A tool that gather steps to fix a computer issue"
        self.embedding_model = DEFAULT_EMBEDDING_MODEL
        self.doc_w_embeddings = self.get_doc_embeddings(
            "src\data\data_test_python.json"
        )
        self.signature = {"text": "str"}

    def get_doc_embeddings(self, documents_path):
        # should be replaced by proper vector database
        doc_w_embeddings = []
        with open(documents_path, "r") as doc_file:
            documents = json.load(doc_file)
        for doc in documents["troubleshooting_scenarios"]:
            embedding = client.embeddings.create(
                model=self.embedding_model,
                input=f"Issue: {doc['issue']}\n,Steps: {'\n  '.join(s for s in doc["steps"])}",
                encoding_format="float",
            )
            doc["embedding"] = embedding.data[0].embedding
            doc_w_embeddings.append(doc)
        return doc_w_embeddings

    def execute_task(self, task, parameters):
        # should be replaced by proper embedding retrieval
        text_embedding = (
            client.embeddings.create(
                model=self.embedding_model,
                input=parameters["text"],
                encoding_format="float",
            )
            .data[0]
            .embedding
        )
        dist_list = []
        for doc in self.doc_w_embeddings:
            cosine_dist = _compute_cosine_similarity(text_embedding, doc["embedding"])
            dist_list.append(cosine_dist)
        closest_doc = self.doc_w_embeddings[dist_list.index(max(dist_list))]
        doc_as_context = f"Issue: {closest_doc['issue']}\n,Steps: {'\n  '.join(s for s in closest_doc["steps"])}"
        return doc_as_context


class DummyTool:
    def __init__(self, name):
        self.name = name
        self.purpose = "A tool for testing purposes."
        self.signature = {"answer": "int"}

    def execute_task(self, task, parameters):
        return f"Test completed. The parameters is {parameters['answer']}"
