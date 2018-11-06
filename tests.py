import unittest

from matchlp import *

class MyTest(unittest.TestCase):
    def setUp(self):
        self.data = {
            "name::John": {
                "5": "T",
                "2": "L",
                "3": "I"
            },
            "name::Mary": {
                "2": "T",
                "5": "I"
            },
            "name::Alice": {
                "5": "L",
                "3": "T",
            }
        }

    def test_data_to_concepts(self):
        concepts = data_to_concepts(self.data)
        self.assertEqual(set(concepts), set(["2","3","5"]))

    def test_data_to_graph(self):

        G = data_to_graph(self.data)
        self.assertEqual(len(G.edges), 10)
        self.assertEqual(len(G.nodes), 10)

if __name__ == '__main__':
    unittest.main()
