from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from Node import Node
from Edge import Edge
import networkx as nx
import matplotlib.pyplot as plt



G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2, 3])
G.add_edge(1, 2)
e = (2, 3)
G.add_edge(*e)  # unpack edge tuple*
G = nx.petersen_graph()
#vplt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
plt.show()

d = {"123": 4, 4:"dd"}
node = Node(1)
d[1] = node

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [l1, l2]

print(Edge(1,2,5))

g = DiGraph()  # creates an empty directed graph
for n in range(4):
    g.add_node(n)
g.add_edge(0, 1, 1)
g.add_edge(1, 0, 1.1)
g.add_edge(1, 2, 1.3)
g.add_edge(2, 3, 1.1)
g.add_edge(1, 3, 1.9)
g.remove_edge(1, 3)
g.add_edge(1, 3, 10)
print(g)  # prints the __repr__ (func output)
print(g.get_all_v())  # prints a dict with all the graph's vertices.
print(g.all_in_edges_of_node(1))
print(g.all_out_edges_of_node(1))
g_algo = GraphAlgo(g)
#print(g_algo.shortest_path(0, 3))
#g_algo.plot_graph()

s = """{"Edges":[{"src":12453,"w":45.970607092631596,"dest":954845}, ...], "Nodes":[{"id":0}, ...]}"""
print(g_algo.get_src(s))

print(g_algo.get_weight(s))

print(g_algo.get_dest(s))

edg = zip(g_algo.get_edges(GraphAlgo.get_edges(r)))

print(GraphAlgo.get_edges(r))
x = []

