import unittest
from agents.agent1 import agent1
from agents.agent2 import agent2

class TestAgents(unittest.TestCase):
    def test_agent1_response(self):
        self.assertEqual(agent1.respond("Hello"), "Agent 1 received: Hello")

    def test_agent2_response(self):
        self.assertEqual(agent2.respond("Hello"), "Agent 2 received: Hello")

if __name__ == '__main__':
    unittest.main()
