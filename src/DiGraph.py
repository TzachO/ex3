from GraphInterface import GraphInterface
from Node import Node
from Edge import Edge

class DiGraph(GraphInterface):
    """description of class"""

    def __init__(self):
        self.nodes = {}
        self.edges = []
        self._MC = 0

    def __repr__(self):
        return "Nodes: " + str(self.nodes) + "\nEdges: " + str(self.edges)

    #done
    def v_size(self) -> int:
        """
        Returns the number of vertices in this graph
        @return: The number of vertices in this graph
        """

        return len(self.nodes)

    #done
    def e_size(self) -> int:
        """
        Returns the number of edges in this graph
        @return: The number of edges in this graph
        """
        
        return len(self.edges)

    #done
    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)
        """

        return self.nodes

    #done
    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """

        return {edge.src:edge.weight for edge in self.edges if edge.dest == id1}

    #done
    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from id1, each node is represented using a pair
        (other_node_id, weight)
        """

        return {edge.src:edge.weight for edge in self.edges if edge.dest == id1}

    #done
    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        
        return self._MC

    #done
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
            self.edges.append(Edge(id1, id2, weight))
            self._MC += 1
            return True

        return False

     #done
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

        self.nodes[node_id] = Node(node_id, pos)
        self._MC += 1

        return True

    #done
    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.

        Note: if the node id does not exists the function will do nothing
        """
        
        if node_id in self.nodes.keys():
            self.nodes.pop(node_id)

            i = 0
            while i < len(self.edges):
                if self.is_in_edge(node_id, self.edges[i]):
                        self.edges.pop(i)
                        i -= 1

                i += 1
            
            self._MC += 1
            return True

        return False

    #done
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
            self.edges.pop(index)
            self._MC += 1
            return True

        return False
        
    #done
    def find_edge(self, id1: int, id2: int) -> int:
        for edge, i in zip(self.edges, range(len(self.edges))):
            if edge.src == id1 and edge.dest == id2:
                return i

        return -1

    # done 
    def is_node_exist(self, node_id: int) -> bool:
        for id in self.nodes.keys():
            if id == node_id:
                return True
        
        return False

    #done
    def is_in_edge(self, node_id: int, edge: Edge) -> bool:
        if edge.src == node_id or edge.dest == node_id:
            return True

        return False

