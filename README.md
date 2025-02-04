# homework-digitalkin
The goal is to develop a 'Customer Service' chatbot that answers client inquiries, either directly or by retrieving relevant context from a document outlining common IT issues. The unique aspect of this project is its use of the 'Agentic Mesh' architecture. In this setup, an AI Agent handles the question and determines whether it has enough information to respond or if it needs additional context from another AI Agent specialized in context retrieval.

This work is strongly inspired by [From Isolated AI to Agentic Mesh: The Next Technological Leap](https://medium.com/digitalkin/from-isolated-ai-to-agentic-mesh-the-next-technological-leap-31a6333ecc77) by Thibaud Perrin and [The Anatomy of an Autonomous Agent](https://medium.com/towards-data-science/the-anatomy-of-an-autonomous-agent-499b42b73124) by Eric Broda.

You can find more details (instructions, my synthesis, detailed specs) in the "documents" folder. There is also a synthesis on several Medium articles used for this project, along with detailed technical specs.

It is **strongly advised** to create a virtual env (Python 3.12) for the project :
```
$ python -m venv .venv
```
To install the dependencies listed in `pyproject.toml`
```
$ pip install .
```

**DO NOT FORGET** to put your `OPENAI_API_KEY` in a `.env` file in the root folder.

To run the interface locally:
```
$ streamlit run src/app.py
```
To test: 
```
$ pytest
```


