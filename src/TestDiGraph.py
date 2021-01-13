import unittest
from DiGraph import DiGraph
from Node import Node
from Edge import Edge

class Test_TestDiGraph(unittest.TestCase):

    def test___repr__(self):
        return

    def test_v_size(self):
        return

    def test_e_size(self):
        return

    def test_get_all_v(self):
        return

    def test_all_in_edges_of_node(self):
        return

    def test_all_out_edges_of_node(self):
        return

    def test_get_mc(self):
        return

    def test_add_edge(self):
        return

    def test_add_node(self):
        return

    def test_remove_node(self):
        return

    def test_remove_edge(self):
        return
        
    def test_find_edge(self):
        return

    def test_is_node_exist(self):
        return

    def test_is_in_edge(self):
        return

    def test_get_transpose(self):
        g = generate_graph()
        gt = g.transpose()

        E1 = g.get_all_edges()
        E2 = gt.get_all_edges()

        for e1, e2 in zip(E1, E2):
            self.assertEqual(e1.src, e2.dest)
            self.assertEqual(e1.dest, e2.src)
            self.assertEqual(e1.weight, e2.weight)
        return

def generate_graph():
    g = DiGraph()
    for i in range(1, 6):
        g.add_node(i)

    g.add_edge(1, 2, 6)
    g.add_edge(1, 4, 1)

    g.add_edge(2, 1, 6)
    g.add_edge(2, 3, 5)
    g.add_edge(2, 4, 2)
    g.add_edge(2, 5, 2)

    g.add_edge(3, 2, 5)
    g.add_edge(3, 5, 5)

    g.add_edge(4, 1, 1)
    g.add_edge(4, 2, 2)
    g.add_edge(4, 5, 1)

    g.add_edge(5, 2, 2)
    g.add_edge(5, 3, 5)
    g.add_edge(5, 4, 1)

    return g

if __name__ == '__main__':
    unittest.main()
