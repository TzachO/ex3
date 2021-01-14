import time
import networkx as nx
import matplotlib.pyplot as plt
from GraphAlgo import GraphAlgo
import json

def scc_time():
    g = GraphAlgo()
    f = "TestFiles//no pos//G_10_80_0.json"
    g.load_from_json(f)

    start = time.time()
    g.connected_components()
    end = time.time()
    our_time_elapsed = end - start

    g = get_graph_from_json(f)
    start = time.time()
    nx.strongly_connected_components(g)
    end = time.time()
    nx_time_elapsed = end - start

    print("Our SCC algo time (s): " + str(our_time_elapsed) + "\t|\tnetworkx's SCC algo time: " + str(nx_time_elapsed))

def shortest_path_time():
    g = GraphAlgo()
    f = "TestFiles//rand pos//G_10_80_2.json"
    g.load_from_json(f)

    start = time.time()
    g.shortest_path(1, 7)
    end = time.time()
    our_time_elapsed = end - start

    g = get_graph_from_json(f)
    start = time.time()
    nx.shortest_path(g, source=1, target=7, method='dijkstra')
    end = time.time()
    nx_time_elapsed = end - start

    print("Our dijkstra algo time (s): " + str(our_time_elapsed) + "\t\t|\tnetworkx's dijkstra algo time: " + str(nx_time_elapsed))

def plot_time():
    g = GraphAlgo()
    f = "TestFiles//rand pos//G_10_80_2.json"
    g.load_from_json(f)

    start = time.time()
    g.plot_graph()
    end = time.time()
    our_time_elapsed = end - start

    g = get_graph_from_json(f)
    start = time.time()
    nx.draw(g, pos=nx.circular_layout(g), node_color='r', edge_color='b')
    end = time.time()
    nx_time_elapsed = end - start

    print("Our plotting time (s): " + str(our_time_elapsed) + "\t\t|\tnetworkx's plotting time (s): " + str(nx_time_elapsed))
    

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
    nx.shortest_path(g, source=1, target=7, method='dijkstra')

def main():
    scc_time()
    shortest_path_time()
    plot_time();
    return

if __name__ == '__main__':
    main()
