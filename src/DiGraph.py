from GraphInterface import GraphInterface
from Node import Node
from Edge import Edge
import DiGraph # imported, so we can define a return type "DiGraph" of a function. i.e, def foo(self) -> DiGraph:

class DiGraph(GraphInterface):
    """a graph implementation that supporsts basic operations on a graph"""

    def __init__(self):
        self.__nodes = [] 
        self.__nodes_dict = {}
        self.__edges = []
        self._MC = 0

    def __repr__(self):
        return """{"Edges": """ + str(self.__edges) + ""","Nodes": """ + str(self.__nodes) + "}"

    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """

        return len(self.__nodes)

    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        
        return len(self.__edges)

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """

        # return {node.id:node for node in self.__nodes}
        return self.__nodes_dict

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """

        return {edge.src:edge.weight for edge in self.get_all_edges() if edge.dest == id1}

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from id1, each node is represented using a pair
        (other_node_id, weight)
        """

        return {edge.dest:edge.weight for edge in self.__edges if edge.src == id1}

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        
        return self._MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.

        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if self.find_edge(id1, id2) >= 0:
            return False

        if self.is_node_exist(id1) and self.is_node_exist(id2):
            self.__edges.append(Edge(id1, id2, weight))
            self._MC += 1
            return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.

        Note: if the node id already exists the node will not be added
        """
        if self.is_node_exist(node_id):
            return False

        node = Node(node_id, pos)

        self.__nodes.append(node)
        self.__nodes_dict[node_id] = node
        self._MC += 1

        return True
        
    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        
        if node_id in self.get_all_v():
            self.__nodes.pop(node_id)
            self.__nodes_dict.pop(node_id)

            i = 0
            while i < len(self.__edges):
                if self.is_in_edge(node_id, self.__edges[i]):
                    self.__edges.pop(i)
                    i -= 1

                i += 1
            
            self._MC += 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.

        Note: If such an edge does not exists the function will do nothing
        """
        index = self.find_edge(node_id1, node_id2)
        if index != -1:
            self.__edges.pop(index)
            self._MC += 1
            return True

        return False

    def find_edge(self, id1: int, id2: int) -> int:
        """
        Finds the index of the first occurence of an edge.
        @param id1: source node id of the edge to find
        @param id2: destination node id of the edge to find
        @return: index of the first occurence of the edge. if not found, returns -1
        """

        for edge, i in zip(self.__edges, range(len(self.__edges))):
            if edge.src == id1 and edge.dest == id2:
                return i

        return -1

    def is_node_exist(self, node_id: int) -> bool:
        """
        Determines if a node exists in the graph
        @param node_id: id of the node
        @return: True if the node was found in the graph. otherwise, returns False.
        """

        for id in self.get_all_v():
            if id == node_id:
                return True
        
        return False

    def is_in_edge(self, node_id: int, edge: Edge) -> bool:
        """
        Determines if a node is one of an edge's vertices.
        @param node_id: id of the node
        @param node_id: edge to investigate
        @return: True if the node is either the source or destination of an edge. otherwise, returns False.
        """

        if edge.src == node_id or edge.dest == node_id:
            return True

        return False

    def get_all_edges(self) -> list:
        """
        Gets all the graph's edges
        @return: a list all the graph's edges
        """

        return self.__edges

    def get_nodes(self) -> list:
        """
        Gets all the graph's nodes
        @return: a list of all the nodes' objects in the graph
        """

        return self.__nodes

    def get_node(self, node_id: int) -> Node:
        return self.get_all_v()[node_id]

    def get_transpose(self, f: list = None) -> DiGraph:
        """
        Gets the transpose of the graph. i.e, the original graph who's all its edges are inverted.
        @param f: a list of finish times calculated by running DFS on the graph
        @return: a transpose of a graph. if param f was given - the order of the nodes of the graph will be by descending order of
        """
        nodes = []
        if f != None:
            nodes = [(key, f[key]) for key in f.keys()]
            nodes.sort(key=lambda tup: tup[1], reverse=True)
            nodes = [self.get_node(tup[0]) for tup in nodes]
        else:
            nodes = self.get_nodes()

        g = DiGraph()
        for node in nodes:
            g.add_node(node.id, node.pos)

        for edge in self.__edges:
            g.add_edge(edge.dest, edge.src, edge.weight)

        return g

class Edge(object):
    """description of class"""
    
    def __init__(self, id1: int, id2: int, weight: float):
        self.src = id1
        self.dest = id2
        self.weight = weight

    def __repr__(self):
        return """{"src":""" + str(self.src) + ""","w":""" + str(self.weight) + ""","dest":""" + str(self.dest) + "}"

class Node(object):
    """description of class"""

    def __init__(self, id: int, pos: tuple = None):
        self.id = id
        self.pos = pos
        self.data = 0

    def __repr__(self):
        if self.pos == None:
            return """{"id":""" + str(self.id) + "}"
        
        # {"pos":"0.08170009195216499,0.7541519252293025,0.0","id":0}
        return """{"pos":\"""" + str(self.pos[0]) + "," + str(self.pos[1]) + "," + str(self.pos[2]) + """\","id":""" + str(self.id) + "}"