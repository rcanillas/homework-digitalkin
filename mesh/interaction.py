from agents.agent1 import agent1
from agents.agent2 import agent2

def communicate(message):
    response1 = agent1.respond(message)
    response2 = agent2.respond(response1)
    return response2
