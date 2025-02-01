from abc import ABC, abstractmethod
from flask import Flask, request, jsonify

app = Flask(__name__)


class AgentBase(ABC):
    def __init__(self, name, description, tools, model, authorizations, state, memory):
        self.name = name
        self.description = description
        self.tools = tools
        self.model = model
        self.authorizations = authorizations
        self.state = state
        self.memory = memory

    @abstractmethod
    def analyze(self, data):
        pass

    @abstractmethod
    def plan(self, objective):
        pass

    @abstractmethod
    def validate(self, objective):
        pass

    @abstractmethod
    def execute(self, plan):
        pass

    @abstractmethod
    def execute_task(self, task_data):
        pass

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
                                                    "tools": {"type": "array", "items": {"type": "string"}},
                                                    "model": {"type": "string"},
                                                    "authorizations": {"type": "array", "items": {"type": "string"}},
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
                            }
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
        return jsonify({"status": "Task received", "data": task_data})

    @app.route("/observations", methods=["GET"])
    def get_observations(self):
        return jsonify({"usage": "Metrics data here", "history": "History data here"})

    def run(self):
        app.run(debug=True)
