class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.distance = 0
        self.color = 'black'

    def add_neighbor(self, V):
        if V not in self.neighbors:
            self.neighbors.append(V)
            self.neighbors.sort()

