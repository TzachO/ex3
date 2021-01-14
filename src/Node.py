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