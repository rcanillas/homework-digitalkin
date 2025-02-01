from agents.CustomerServiceAgent import CustomerServiceAgent
from agents.TechnicalSupportAgent import TechnicalSupportAgent

def communicate(message):
    response = CustomerServiceAgent.respond(message)
    return response
