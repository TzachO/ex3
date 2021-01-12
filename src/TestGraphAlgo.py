import unittest

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
        g_algo.load_from_json("""C:\\Users\\elyas\\OneDrive\\Documents\\Visual Studio Projects\\Graphs\\Graphs\\TestFiles\\no pos\\G_10_80_0.json""")
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

    def test_shortest_path(self):
        g_algo = GraphAlgo()
        g_algo.add_node(0)
        g_algo.add_node(1)
        g_algo.add_node(2)
        g_algo.add_edge(0,1,1)
        g_algo.add_edge(1,2,4)
        res = g_algo.shortest_path(0,1)
        #self.assertEqual(res, (1, [0, 1]))

        return

    def test_connected_component(self):
        return

    def test_connected_components(self):
        return

    def test_plot_graph(self):
        return

    def test_get_src(self):
        return

    def test_get_weight(self):
        return

if __name__ == '__main__':
    unittest.main()
