from Node import Node

class Edge(object):
    """description of class"""
    
    def __init__(self, id1: int, id2: int, weight: float):
        self.edge = (id1, id2)
        self.weight = weight

    def __repr__(self):
        return str((self.edge, self.weight))