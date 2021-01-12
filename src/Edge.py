from Node import Node

class Edge(object):
    """description of class"""
    
    def __init__(self, id1: int, id2: int, weight: float):
        self.src = id1
        self.dest = id2
        self.weight = weight

    def __repr__(self):
        return """{"src":""" + str(self.src) + ""","w":""" + str(self.weight) + ""","dest":""" + str(self.dest) + "}"