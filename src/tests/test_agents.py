import unittest
from agents.customer_service_agent import CustomerServiceAgent
from agents.technical_support_agent import TechnicalSupportAgent

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.cs_agent = CustomerServiceAgent()
        self.ts_agent = TechnicalSupportAgent()

    def test_CustomerServiceAgent_response(self):
        self.assertEqual(self.cs_agent.respond("Hello"), "Customer Service Agent received: Hello")

    def test_TechnicalSupportAgent_response(self):
        self.assertEqual(self.ts_agent.respond("Hello"), "Technical Support Agent received: Hello")

    def test_analyze_function(self):
        user_message = "I need help with my computer."
        parameters = {"urgency": "high"}
        tool_specifications = [
            {"name": "Conversation Tool", "purpose": "Answer user questions"},
            {"name": "Context Retrieval Tool", "purpose": "Retrieve relevant documents"},
        ]
        agent_memory = {"previous_tasks": []}

        best_tools = self.ts_agent.analyze(user_message, parameters, tool_specifications, agent_memory)
        expected_tools = ["Context Retrieval Tool"]  # Assuming this is the expected output

        self.assertEqual(best_tools, expected_tools)

if __name__ == '__main__':
    unittest.main()
