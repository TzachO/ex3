import json
from Edge import Edge
from Node import Node
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph
import matplotlib.pyplot as plt

g = DiGraph()
g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_edge(1,1, 3)
g.add_edge(1,2,4)
g_algo = GraphAlgo()

f = """C:\\Users\\elyas\\OneDrive\\Documents\\Visual Studio Projects\\Graphs\\Graphs\\TestFiles\\rand pos\\G_10_80_2.json"""
g_algo.load_from_json(f)
print(g_algo._GraphAlgo__get_pos("1,2,3"))

nodes = g_algo.get_nodes()
print(nodes)


g_algo.plot_graph()


G = GraphAlgo()