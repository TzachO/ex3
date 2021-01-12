import unittest
from DiGraph import DiGraph


class Test_tests(unittest.TestCase):
    def add_node(self):
        g = DiGraph()
        g.add_node(1)
        self.assertEqual(g.v_size(), 2)

if __name__ == '__main__':
    unittest.main()

    
