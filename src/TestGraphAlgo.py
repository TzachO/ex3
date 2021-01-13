import unittest

from mytools import *

from Node import Node
from Edge import Edge
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

class Test_TestGraphAlgo(unittest.TestCase):

    def test_get_graph(self):
        
        return

    #done
    def test_load_from_json(self):
        g_algo = GraphAlgo(DiGraph())
        g_algo.load_from_json("""TestFiles\\no pos\\G_10_80_0.json""")
        self.assertEqual(len(g_algo.get_graph().get_all_v()), 10)

        return

    #done
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

    #done
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
        ga = generate_graph()
        ga.connected_component(1)
        return

    def test_connected_components(self):
        return

    def test_plot_graph(self):
        return

    def test_get_src(self):
        return

    def test_get_weight(self):
        return

    def test_DFS(self):
        ga = generate_graph()
        color, p, d, f = ga.DFS()
        l = [(key,d[key]) for key in d.keys()]
        l = sort_tuple(l)
        y = l


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


if __name__ == '__main__':
    unittest.main()
