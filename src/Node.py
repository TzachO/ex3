class Node(object):
    """description of class"""

    def __init__(self, id: int, pos: tuple = None):
        self.id = id
        self.pos = pos
        self.data = 0

    def __repr__(self):
        return str(self.id)
