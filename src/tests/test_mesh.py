import unittest
from mesh.interaction import communicate

class TestMesh(unittest.TestCase):
    def test_communication(self):
        self.assertEqual(communicate("Hello"), "Technical Support Agent received: Customer Service Agent received: Hello")

if __name__ == '__main__':
    unittest.main()
