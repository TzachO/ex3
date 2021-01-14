import unittest

from Node import Node
from Edge import Edge
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

class Test_TestGraphAlgo(unittest.TestCase):

    def test_get_graph(self):
        
        return

    def test_load_from_json(self):
        g_algo = GraphAlgo(DiGraph())
        g_algo.load_from_json("""TestFiles\\no pos\\G_10_80_0.json""")
        self.assertEqual(len(g_algo.get_graph().get_all_v()), 10)

    def test_save_to_json(self):
        g = DiGraph()
        for i in range(4):
            g.add_node(i)
        g.add_edge(1,2,3)
        g.add_edge(2,3,4)
        g.add_edge(1,3,5)
        g.add_edge(3,4,6)
        g_algo = GraphAlgo(g)

        f = "save_to_json_test.json"
        g_algo.save_to_json(f)

        g_algo_2 = GraphAlgo(DiGraph())
        g_algo_2.load_from_json(f)

        nodes1 = g_algo.get_graph().get_all_v()
        edges1 = g_algo.get_graph().get_all_edges()

        nodes2 = g_algo_2.get_graph().get_all_v()
        edges2 = g_algo_2.get_graph().get_all_edges()

        for k1, k2 in zip(nodes1, nodes2):
            self.assertEqual(repr(nodes1[k1]), repr(nodes2[k2]))

        for e1, e2 in zip(edges1, edges2):
            self.assertEqual(repr(e1), repr(e2))

        

        return

    def test_shortest_path(self):
        ga = generate_graph()
        res = ga.shortest_path(1,5)

        self.assertEqual(res, (2, [1, 4, 5]))

        g_algo = GraphAlgo()
        g_algo.add_node(0)
        g_algo.add_node(1)
        g_algo.add_node(2)
        g_algo.add_edge(0,1,1)
        g_algo.add_edge(1,2,4)
        self.assertEqual(g_algo.shortest_path(0,1), (1, [0, 1]))
        self.assertEqual(g_algo.shortest_path(0,2), (5, [0, 1, 2]))

    def test_connected_component(self):
        ga = generate_graph2()
        scc = ga.connected_component(1)
        self.assertEqual(repr(scc), repr([0, 1, 2]))

    def test_connected_components(self):
        ga = generate_graph2()
        SCCs = ga.connected_components()
        self.assertEqual(repr(SCCs), repr([[0, 1, 2], [3], [4]]))

    def test_plot_graph(self):
        ga = generate_graph2()
        # ga.plot_graph()
        return

    def test_DFS(self):
        ga = generate_graph()
        ga.add_node(7)
        color, p, d, f = ga.DFS()
        self.assertEqual(repr(color), repr({1: 'b', 2: 'b', 3: 'b', 4: 'b', 5: 'b', 7: 'b'}))
        self.assertEqual(repr(p), repr({1: None, 2: 1, 3: 2, 4: 5, 5: 3, 7: None}))
        self.assertEqual(repr(d), repr({1: 1, 2: 2, 3: 3, 5: 4, 4: 5, 7: 11}))
        self.assertEqual(repr(f), repr({4: 6, 5: 7, 3: 8, 2: 9, 1: 10, 7: 12}))

    def test_clear(self):
        g_algo = GraphAlgo(DiGraph())
        g_algo.load_from_json("""TestFiles\\no pos\\G_10_80_0.json""")
        self.assertEqual(len(g_algo.get_graph().get_all_v()), 10)

        g_algo.clear()
        self.assertEqual(repr(g_algo), repr(GraphAlgo()))

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

    return GraphAlgo(g)

def generate_graph2():
    g = DiGraph()
    for i in range(5):
        g.add_node(i)

    g.add_edge(0, 2, 1)
    g.add_edge(0, 3, 1)

    g.add_edge(1, 0, 1)

    g.add_edge(2, 1, 1)

    g.add_edge(3, 4, 1)

    return GraphAlgo(g)

if __name__ == '__main__':
    unittest.main()
