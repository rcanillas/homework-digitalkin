import unittest
from agents.agent1 import CustomerServiceAgent
from agents.agent2 import TechnicalSupportAgent

class TestAgents(unittest.TestCase):
    def test_CustomerServiceAgent_response(self):
        self.assertEqual(CustomerServiceAgent.respond("Hello"), "Customer Service Agent received: Hello")

    def test_TechnicalSupportAgent_response(self):
        self.assertEqual(TechnicalSupportAgent.respond("Hello"), "Technical Support Agent received: Hello")

if __name__ == '__main__':
    unittest.main()
