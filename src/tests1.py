from DiGraph import DiGraph

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
#print(g)  # prints the __repr__ (func output)
#print(g.get_all_v())  # prints a dict with all the graph's vertices.
#print(g.all_in_edges_of_node(1))
#print(g.all_out_edges_of_node(1))
#g_algo = GraphAlgo(g)
#print(g_algo.shortest_path(0, 3))
#g_algo.plot_graph()

print(g.all_out_edges_of_node(1))

x = []
