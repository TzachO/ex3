import unittest
from DiGraph import DiGraph
from Node import Node
from Edge import Edge

class Test_TestDiGraph(unittest.TestCase):

    def test___repr__(self):
        g = DiGraph()
        self.assertEqual(repr(g), """{"Edges": [],"Nodes": []}""")

        g.add_node(1)
        self.assertEqual(repr(g), """{"Edges": [],"Nodes": [{"id":1}]}""")

        g.add_node(2)
        self.assertEqual(repr(g), """{"Edges": [],"Nodes": [{"id":1}, {"id":2}]}""")

        g.add_edge(1, 2, 1)
        self.assertEqual(repr(g), """{"Edges": [{"src":1,"w":1,"dest":2}],"Nodes": [{"id":1}, {"id":2}]}""")

        g.add_node(3)
        self.assertEqual(repr(g), """{"Edges": [{"src":1,"w":1,"dest":2}],"Nodes": [{"id":1}, {"id":2}, {"id":3}]}""")

        g.add_edge(1,3,2)
        self.assertEqual(repr(g), """{"Edges": [{"src":1,"w":1,"dest":2}, {"src":1,"w":2,"dest":3}],"Nodes": [{"id":1}, {"id":2}, {"id":3}]}""")

    def test_v_size(self):
        g = DiGraph()

        self.assertEqual(g.v_size(), 0)

        for i in range(5):
            g.add_node(i)

        self.assertEqual(g.v_size(), 5)

    def test_e_size(self):
        g = DiGraph()
        self.assertEqual(g.e_size(), 0)

        g = generate_graph()
        self.assertEqual(g.e_size(), 14)

    def test_get_all_v(self):
        g = generate_graph2()
        self.assertEqual(repr(g.get_all_v()), repr({node.id:node for node in g.get_nodes()}))

    def test_all_in_edges_of_node(self):
        g = generate_graph2()

        self.assertEqual(repr(g.all_in_edges_of_node(0)), repr({1:1}))
        self.assertEqual(repr(g.all_in_edges_of_node(1)), repr({2:1}))
        self.assertEqual(repr(g.all_in_edges_of_node(2)), repr({0:1}))
        self.assertEqual(repr(g.all_in_edges_of_node(3)), repr({0:1}))
        self.assertEqual(repr(g.all_in_edges_of_node(4)), repr({3:1}))

    def test_all_out_edges_of_node(self):
        g = generate_graph2()

        self.assertEqual(repr(g.all_out_edges_of_node(0)), repr({2:1, 3:1}))
        self.assertEqual(repr(g.all_out_edges_of_node(1)), repr({0:1}))
        self.assertEqual(repr(g.all_out_edges_of_node(2)), repr({1:1}))
        self.assertEqual(repr(g.all_out_edges_of_node(3)), repr({4:1}))
        self.assertEqual(repr(g.all_out_edges_of_node(4)), repr({}))

    def test_get_mc(self):
        g = DiGraph()

        self.assertEqual(g.get_mc(), 0)

        g.add_node(0)
        g.add_node(1)
        self.assertEqual(g.get_mc(), 2)

        g.add_edge(0, 1, 1)
        self.assertEqual(g.get_mc(), 3)

        g.add_node(2)
        g.add_node(3)
        g.add_edge(2, 3, 1)
        self.assertEqual(g.get_mc(), 6)

        g.remove_edge(2,3)
        self.assertEqual(g.get_mc(), 7)

        g.remove_node(0)
        self.assertEqual(g.get_mc(), 8)

        return

    def test_add_edge(self):
        g = DiGraph()

        g.add_node(0)
        g.add_node(1)

        g.add_edge(0, 1, 1)
        self.assertEqual(repr(g.get_all_edges()[0]), repr(Edge(0, 1, 1)))

        g.add_edge(1, 0, 1)
        self.assertEqual(len(g.get_all_edges()), 2)

    def test_add_node(self):
        g = DiGraph()

        g.add_node(0)
        self.assertEqual(repr(g.get_nodes()[0]), repr(Node(0, None)))

        g.add_node(1, (1,2,3))
        self.assertEqual(repr(g.get_nodes()[1]), repr(Node(1, (1,2,3))))

        g.add_node(2)
        self.assertEqual(len(g.get_nodes()), 3)

    def test_remove_node(self):
        g = DiGraph()

        g.add_node(0)
        self.assertEqual(repr(g.get_nodes()[0]), repr(Node(0, None)))
        self.assertEqual(len(g.get_nodes()), 1)
        
        g.remove_node(0)
        self.assertEqual(len(g.get_nodes()), 0)

    def test_remove_edge(self):
        g = DiGraph()

        g.add_node(0)
        g.add_node(1)

        g.add_edge(0, 1, 1)
        self.assertEqual(repr(g.get_all_edges()[0]), repr(Edge(0, 1, 1)))

        g.add_edge(1, 0, 1)
        self.assertEqual(len(g.get_all_edges()), 2)

        g.remove_edge(0, 1)
        self.assertEqual(repr(g.get_all_edges()[0]), repr(Edge(1, 0, 1)))
        self.assertEqual(len(g.get_all_edges()), 1)
        
    def test_find_edge(self):
        g = generate_graph2()
        self.assertEqual(g.find_edge(0, 3), 1)
        self.assertEqual(g.find_edge(4, 4), -1)

    def test_is_node_exist(self):
        g = generate_graph2()
        for i in range(5):
            self.assertEqual(g.is_node_exist(i), True)

        self.assertEqual(g.is_node_exist(5), False)

    def test_is_in_edge(self):
        g = generate_graph2()
        self.assertEqual(g.is_in_edge(0, Edge(0, 3, 1)), True)
        self.assertEqual(g.is_in_edge(1, Edge(0, 3, 1)), False)

    def test_get_transpose(self):
        g = generate_graph()
        gt = g.get_transpose()

        E1 = g.get_all_edges()
        E2 = gt.get_all_edges()

        for e1, e2 in zip(E1, E2):
            self.assertEqual(e1.src, e2.dest)
            self.assertEqual(e1.dest, e2.src)
            self.assertEqual(e1.weight, e2.weight)

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

def generate_graph2():
    g = DiGraph()
    for i in range(5):
        g.add_node(i)

    g.add_edge(0, 2, 1)
    g.add_edge(0, 3, 1)

    g.add_edge(1, 0, 1)

    g.add_edge(2, 1, 1)

    g.add_edge(3, 4, 1)

    return g

if __name__ == '__main__':
    unittest.main()
