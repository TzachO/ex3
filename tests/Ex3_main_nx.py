import networkx as nx
import matplotlib.pyplot as plt
from GraphAlgo import GraphAlgo
import json
from networkx.readwrite import json_graph


def check():
    """
    Graph: |V|=4 , |E|=5
    {0: 0: |edges out| 1 |edges in| 1, 1: 1: |edges out| 3 |edges in| 1, 2: 2: |edges out| 1 |edges in| 1, 3: 3: |edges out| 0 |edges in| 2}
    {0: 1}
    {0: 1.1, 2: 1.3, 3: 10}
    (3.4, [0, 1, 2, 3])
    [[0, 1], [2], [3]]
    (2.8, [0, 1, 3])
    (inf, [])
    2.062180280059253 [1, 10, 7]
    17.693921758901507 [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]
    11.51061380461898 [20, 21, 32, 31, 30, 29, 14, 13, 3, 2]
    inf []
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]]
    """
    check0()
    check1()
    check2()


def check0():
    g = nx.DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, weight=1)
    g.add_edge(1, 0, weight=1.1)
    g.add_edge(1, 2, weight=1.3)
    g.add_edge(2, 3, weight=1.1)
    g.add_edge(1, 3, weight=1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, weight=10)
    print(g)  
    print(g.nodes)  
    print(g.in_edges(1))
    print(g.in_edges(1))
    print(nx.dijkstra_path(g, 0, 3))
    nx.draw(g, pos=nx.circular_layout(g), node_color='r', edge_color='b')
    plt.show()

def check1():
    file = "TestFiles/data/T0.json"
    g = get_graph_from_json(file)
    
    print(nx.dijkstra_path(g, 0, 3))
    # print(nx.dijkstra_path(g, 3, 1)) # no path from 3 to 1, therefor an exxception has been thrown
    t = file.split('.')
    #g_algo.save_to_json(t[0]+ '_saved' + '.' + t[1])
    nx.draw(g, pos=nx.circular_layout(g), node_color='r', edge_color='b')
    plt.show()


def check2():
    g = nx.DiGraph()
    file = 'TestFiles/data/A5'
    g = get_graph_from_json(file)
    g.remove_edge(13, 14)
    #g_algo.save_to_json(file + "_edited")
    #a = json_graph.node_link_data(g)
    path = nx.shortest_path(g, source=1, target=7, method='dijkstra')
    print(path)
    path = nx.shortest_path(g, source=47, target=19, method='dijkstra')
    print(path)
    path = nx.dijkstra_path(g, 20, 2)
    print(path)
    #path = nx.dijkstra_path(g, 2, 20) # no path to 20. exception has been thrown
    #print(path)
    #print(g_algo.connected_component(0)) # networkx doesnt have a connencted_component implementation
    #print(g_algo.connected_components())
    print(list(nx.strongly_connected_components(g)))
    nx.draw(g, pos=nx.circular_layout(g), node_color='r', edge_color='b')
    plt.show()

def get_graph_from_json(filename: str) -> nx.DiGraph():
    def get_pos(pos_s: str) -> tuple:
            i = pos_s.find(',')
            x = float(pos_s[:i])

            pos_s = pos_s[i + 1:]
            i = pos_s.find(',')
            y = float(pos_s[:i])

            pos_s = pos_s[i + 1:]
            z = float(pos_s)

            return (x, y, z)

    g = nx.DiGraph()

    with open(filename) as f:
        json_s = f.read()
        json_obj = json.loads(json_s)

        for node in json_obj["Nodes"]:
            if "pos" in node.keys():
                pos = get_pos(node["pos"])
                g.add_node(node["id"], pos=pos)
            else:
                g.add_node(node["id"])
            
        
        for edge in json_obj["Edges"]:
            g.add_edge(edge["src"], edge["dest"], weight=edge["w"])

    return g

if __name__ == '__main__':
    check()
