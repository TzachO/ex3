from Node import Node
from Edge import Edge
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import json
import matplotlib.pyplot as plt


from typing import List

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.__graph = graph

    #done
    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """

        return self.__graph

    #done
    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        f = open(file_name)
        json_s = f.read()
        json_obj = json.loads(json_s)

        for node in json_obj["Nodes"]:
            if "pos" in node.keys():
                pos = self.__get_pos(node["pos"])
                self.__graph.add_node(node["id"], pos)
            else:
                self.__graph.add_node(node["id"])
            
        
        for edge in json_obj["Edges"]:
            self.__graph.add_edge(edge["src"], edge["dest"], edge["w"])
        
        f.close()
    
    #done
    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        
        f = open(file_name, "w")

        json_s = """{"Edges":[""" 
        for edge in self.__graph.get_all_edges():
            json_s += repr(edge) + ","
        json_s = json_s[:len(json_s) - 1] # remove last comma

        json_s += """],"Nodes":["""
        nodes = self.__graph.get_all_v()
        for key in nodes:
            json_s += repr(nodes[key]) + ","
        json_s = json_s[:len(json_s) - 1] # remove last comma

        json_s += "]}"

        f.write(json_s)

        f.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through

        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])

        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of.
        @param id1: The node id
        @return: The list of nodes in the SCC

        Notes:
        If the graph is None or id1 is not in the graph, the function should return an empty list []
        """
        raise NotImplementedError

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC

        Notes:
        If the graph is None the function should return an empty list []
        """
        raise NotImplementedError

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        
        self.__plot_nodes()
        self.__plot_edges()

        plt.show()

    def get_edges(self) -> list:
        return self.get_graph().get_all_edges()

    def get_nodes(self) -> dict:
        return self.get_graph().get_all_v()

    def add_node(self, id: int, pos: tuple = None) -> bool:
        return self.__graph.add_node(id, pos)

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        return self.__graph.add_edge(id1, id2, weight)

    def __plot_nodes(self) -> None:
        nodes = self.get_nodes()

        for key in nodes:
            x = nodes[key].pos[0]
            y = nodes[key].pos[1]
            plt.scatter(x, y, marker='o', color=[(31/255, 8/17, 12/17)], s=500)
            plt.text(x-0.0135, y-0.0135, str(key), color="black", fontsize="14")

    def __plot_edges(self) -> None:
        nodes = self.get_nodes()

        for edge in self.get_edges():
            src = nodes[edge.src]
            dest = nodes[edge.dest]
            weight = edge.weight

            src_x = src.pos[0]
            src_y = src.pos[1]

            dest_x = dest.pos[0]
            dest_y = dest.pos[1]

            #plt.arrow(src_x, src_y, dest_x, dest_y)
            #plt.annotate(s='', xy=(dest_x,dest_y), xytext=(0,0), arrowprops=dict(arrowstyle='-|>'))
            plt.plot([src_x, dest_x], [src_y, dest_y])

    @staticmethod
    def __get_pos(pos_s: str) -> tuple:
        i = pos_s.find(',')
        x = float(pos_s[:i])

        pos_s = pos_s[i + 1:]
        i = pos_s.find(',')
        y = float(pos_s[:i])

        pos_s = pos_s[i + 1:]
        z = float(pos_s)

        return (x, y, z)