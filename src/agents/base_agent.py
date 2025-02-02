# from flask import Flask, request, jsonify


from dotenv import load_dotenv


from openai import OpenAI


from pydantic import BaseModel
from typing import List, Dict, Tuple


import json


load_dotenv()


# next step is to implement agents as standalone server


# app = Flask(__name__)


client = OpenAI()


# Should do more of those


class ValidatorAnswer(BaseModel):

    is_valid: bool

    validity_reason: str


class BaseAgent:

    def __init__(self, name, purpose, tools, model, authorizations, signature):

        self.name = name

        self.purpose = purpose

        self.tools = tools

        self.model = model

        # not really needed for now

        self.authorizations = authorizations

        self.state = "created"

        # need to define memory a bit more in details

        self.memory = {}

        # define the interface with the agent (as tool)
        self.signature = signature

    def analyze(self, user_message, parameters):

        tool_specifications = [
            (
                tool.name,
                tool.purpose,
                " with signature:",
                tool.signature,
            )
            for tool in self.tools
        ]

        prompt = (
            f"You are a {self.purpose}."
            f" Based on the user message: '{user_message}', "
            f"the parameters: {json.dumps(parameters)}, "
            f"the tool specifications: {json.dumps(tool_specifications)}, "
            f"and the agent's memory: {json.dumps(self.memory)}, "
            f"determine the best tools to perform your task. Return the answer in a JSON format with the name of the tools. "
        )

        completion = client.chat.completions.create(
            model=self.model,
            temperature=0,
            messages=[{"role": "user", "content": prompt}],
        )

        ## could use structured output here

        response = completion.choices[0].message.content
        # quick & dirty cleaning
        response = response.replace("json", "").replace("```", "")

        tools = json.loads(
            response
        )  # Assuming the response is a JSON array of tool names

        return tools

    def plan(self, user_message, parameters, selected_tools):

        # need to add an interface spec for the tools here

        tool_specifications = [
            (tool.name, tool.purpose)
            for tool in self.tools
            if tool.name in selected_tools["tools"]
        ]

        # This prompt could be made better

        prompt = (
            f"You are a {self.purpose}."
            f" Based on the user message: '{user_message}', "
            f"the parameters: {json.dumps(parameters)}, "
            f"the tool specifications: {json.dumps(tool_specifications)}, "
            f"and the agent's memory: {json.dumps(self.memory)}, "
            f"determine the steps needed to perform your task. A step is a dictionary with a key 'tool' indicating the name of a tool and the key parameters containing a dict with the name and value of"
            f"all the parameters required to invoke the tool based on the tool's signature. A tool can't be invoked without parameters."
            "The step also contains a key 'task' with a short description of the task."
            # "Exemple: [{'tool':'Dummy Tool,'parameters':{'dummy_parameter':'42'}}]"
            f"Do not try to perform the task, just pass along the parameters for execution."
            f"Return the answer in a JSON format as a list of steps that will be executed later. It is always a list even if there is only one item."
        )

        print(prompt)
        completion = client.chat.completions.create(
            model="gpt-4o",
            temperature=0,
            messages=[{"role": "user", "content": prompt}],
        )

        ## could use structured output here
        ## tried it but had to be creative
        response = completion.choices[0].message.content
        # quick & dirty cleaning
        response = response.replace("json", "").replace("```", "")
        plan = json.loads(response)
        return plan

    def execute(self, plan):

        plan_results = []

        # need to account for potential sequentiality later (needing the result of previous steps)
        print(plan)
        for step_id, step in enumerate(plan):
            # probably could do better here
            print(step_id, step)
            tool = [t for t in self.tools if t.name == step["tool"]][0]
            result = tool.execute_task(step["task"], step["parameters"])
            plan_results.append(result)

        return plan_results

    def validate(self, user_message, parameters, plan, result):

        prompt = (
            f"You are a {self.purpose}."
            f" Based on the user message: '{user_message}', "
            f"the parameters: {json.dumps(parameters)}, "
            f"the plan: {json.dumps(plan)}, "
            f"and the agent's result: {json.dumps(result)}, "
            f"and the agent's memory: {json.dumps(self.memory)}"
            f"determine if the plan was correctly executed."
        )

        completion = client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Confirm if the plan and execution are correct for the task.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=0,
            response_format=ValidatorAnswer,
        )

        valid_result = completion.choices[0].message.parsed

        # Could handle that more gracefully

        valid_result_dict = {
            "is_valid": valid_result.is_valid,
            "validity_reason": valid_result.validity_reason,
        }

        return valid_result_dict

    def execute_task(self, task, parameters):
        selected_tools = self.analyze(task, parameters)
        plan = self.plan(task, parameters, selected_tools)
        result = self.execute(plan)
        is_valid = self.validate(task, parameters, plan, result)
        return {"result": result, "validity": is_valid}


"""


    # next step is to implement agents as standalone servers


    @app.route("/specification", methods=["GET"])


    def get_specification(self):



        return jsonify(


            {


                "openapi": "3.0.0",


                "info": {


                    "title": self.name,


                    "description": self.description,


                    "version": "1.0.0",


                },


                "paths": {


                    "/specification": {


                        "get": {


                            "summary": "Get agent specification",


                            "responses": {


                                "200": {


                                    "description": "Agent specification",


                                    "content": {


                                        "application/json": {


                                            "schema": {


                                                "type": "object",


                                                "properties": {


                                                    "name": {"type": "string"},


                                                    "description": {"type": "string"},


                                                    "tools": {


                                                        "type": "array",


                                                        "items": {"type": "string"},


                                                    },


                                                    "model": {"type": "string"},


                                                    "authorizations": {


                                                        "type": "array",


                                                        "items": {"type": "string"},


                                                    },


                                                    "state": {"type": "string"},


                                                    "memory": {"type": "object"},


                                                },


                                            },


                                        }


                                    },


                                }


                            },


                        }


                    },


                    "/tasks": {


                        "post": {


                            "summary": "Post a task to the agent",


                            "requestBody": {


                                "required": True,


                                "content": {


                                    "application/json": {


                                        "schema": {


                                            "type": "object",


                                            "properties": {


                                                "task": {"type": "string"},


                                                "parameters": {"type": "object"},


                                            },


                                        }


                                    }


                                },


                                "responses": {


                                    "200": {


                                        "description": "Task received",


                                        "content": {


                                            "application/json": {


                                                "schema": {


                                                    "type": "object",


                                                    "properties": {


                                                        "status": {"type": "string"},


                                                        "data": {"type": "object"},


                                                    },


                                                }


                                            }


                                        },


                                    }


                                },


                            },


                        }


                    },


                    "/observations": {


                        "get": {


                            "summary": "Get agent observations",


                            "responses": {


                                "200": {


                                    "description": "Agent metrics",


                                    "content": {


                                        "application/json": {


                                            "schema": {


                                                "type": "object",


                                                "properties": {


                                                    "usage": {"type": "string"},


                                                    "history": {"type": "string"},


                                                },


                                            },


                                        }


                                    },


                                }


                            },


                        }


                    },


                },


            }


        )





    @app.route("/tasks", methods=["POST"])


    def post_tasks(self):



        task_data = request.json



        result = self.execute_task(task_data)



        return jsonify({"status": "Task received", "data": result})



    @app.route("/observations", methods=["GET"])


    def get_observations(self):



        return jsonify({"usage": "Metrics data here", "history": "History data here"})



    def run(self):



        app.run(debug=True)
"""
