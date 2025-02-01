from agents.CustomerServiceAgent import CustomerServiceAgent
from agents.TechnicalSupportAgent import TechnicalSupportAgent

def communicate(message):
    response1 = CustomerServiceAgent.respond(message)
    response2 = TechnicalSupportAgent.respond(response1)
    return response2
    return response
