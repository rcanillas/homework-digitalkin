from agents.agent1 import CustomerServiceAgent
from agents.agent2 import TechnicalSupportAgent

def communicate(message):
    response1 = CustomerServiceAgent.respond(message)
    response2 = TechnicalSupportAgent.respond(response1)
    return response2
