# TODO List - Test Digitalkin 
- [x] Toolbox
- [ ] Registry
- [x] Agent base class
- [x] Customer Service Agent
- [x] Technical Support Agent
- [x] "Front" in streamlit
- [ ] Ecosystem deployment (docker-compose ?)

## Toolbox
Notes & assumptions:
Each bot has its own using toolbox. Toolbox is a dict of tool, each tool is a dict with name, purpose, parameters, and exec function (exemple: rag). Other Agent are not yet part of the toolbox, is unique to the agent !
- [x] Implement toolbox for Customer Service Agent (Conversation Tool). This tool takes a text (context + actual question) and use an LLM (gpt4o-mini) to generate an answer.
- [x] Implement toolbox for Technical Support (Context Retrieval Tool). This tool get a text and find the most relevant document in a dict of documents, and returns it.



## Registry 
Notes & assumptions: The registry is a simple server where agents register themselves and their description and get the other agents in the ecosystem. Provide an unique ID for the agent. It could be decentralized later. Also provides trust & performance metrics of the agent (useful for selection later)

- [ ] Implement GET /register function where Agent signal that they want register themselve on the platform. The Registry then send a GET /specification request to the Agent so get its specs in OpenAPI format. The Registry also directly responds a list of the other Agents. 

- [ ] Implement GET /ecosystem to retrieve other agents's spec (in case of update)

- [ ] Implement a Docker file allowing the Registry to be containerized

- [ ] (Optionnal) Set up cron to periodically get agents' updated stats.

## Agent Base class:
Notes & assumptions: main focus of the system. Agent is separated in 3 layers : Communication, Task Management, and State, following the bibliography. They also have a toolbox that is for now internally managed, but could be outsourced.
#### Communication
 A basic Flask server to handle https request (can be updated vith gRPC later)
 - [ ] implement GET /specification where the agent sends its spec in OpenAPI json format (can be changed later)
 - [ ] implement POST /tasks to start the task execution process (specific prompt & parameters are in the body) (potential timeout issue with long response time ?)
 - [ ] implement GET /observations to return agent metrics (usage, history, stats, etc)
 - [ ] (Optional) implement POST /operations to control Agent lifecycle from afar (start/stop/pause/resume/update new params etc)

#### Task Management
This is where the Agent will be "thinking" about the task sent on the /tasks endpoint and select the best tool(s) at its disposition to execute it. It is based on four core functions: analyze, plan, execute, validate. The inputs and outputs of these function are logged in the agent's memory (schema defined in "State" layer). All these function are performed using an internal LLM model unique to the agent (by default, OpenAI's gpt4o-mini for cost)
- [x] implement the logic of the "analyze" function. This function take the prompt and the parameters of the task and the agent, along with the specification of each tool available to the model + the agent's memory, and asks itself "what are the best tools to do this task ?". Optional: if no adapted tool is found, refuse to answer the request.
- [x] Implement the logic of the "plan" function. This function use the tasks of the prompt + parameters + the result of the "analyze" function, and create a sequence
of steps based on the selected tools' specification in a json format.
- [x] Implement the "execute" function that read the json file and gather the outputs of the selected tools.
- [x] Implement the "validate" fonction that takes the input of all other function, validate if the plan was correctly executed, and if the result is coherent with the submitted tasks. Optional: implement retry with corrected plan if error is found. for now return an error if the task in incorrectly executed

#### State
The agent is described by several properties, reflecting the ones of Tools: name, purpose, parameters (if needed), the information needed to understand and utilize the agent, and the agent's purpose. These parameters are compiled in a json in the OpenAPI format. The execution function of the agent is always "execute_task".
The agent is also a state machine with different states: it can be ready, working, complete (& ready again, need to modify the bib here), pending answer from an other agent / humain input, or in error state. 
For now these state are managed in the "Task Management" layer. 
- [ ] Implement state change consistently in the different functions mentioned above.
- [x] Implement "execute_tasks" function that encapsulates the previous function and is called when an HTTP POST request is made on the /tasks endpoint.

## CS Agent
Notes & assumptions : this is the implementation of the fist agent. It only has one tool: a Conversation Tool (see Toolbox session). It has access to other agents.
- [ ] Implement the flask server specific for this agent.
- [ ] Implement a Docker file allowing the Agent to be containerized
 
## TS Agent:
Notes & assumptions: this is the implementation of the second agent. It has access to only one tool: "Context Retrieval Tool". Its job is to take a question and to forward the best matching document found by the tool to the source of the question.
- [ ] Implement the flask server specific for this agent.
- [ ] Implement a Docker file allowing the Agent to be containerized


## Front Streamlit:
Notes & assumptions: Optionnal. The front is a simple chat interface where the user can ask question to the Customer Service agent.
- [ ] Implement a minimal interface using REST call to the agent (deployed in a container on the same machine)


## Ecosystem deployment:
-   Notes & assumptions: the different parts of the Mesh (Agents & Registry) are containerized as docker on the same machine and communicating through the REST API.
- [ ] Implement a docker-compose file that deploys all the necesery part of the Mesh
