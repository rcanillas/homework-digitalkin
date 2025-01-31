import unittest
from mesh.interaction import communicate

class TestMesh(unittest.TestCase):
    def test_communication(self):
        self.assertEqual(communicate("Hello"), "Agent 2 received: Agent 1 received: Hello")

if __name__ == '__main__':
    unittest.main()
