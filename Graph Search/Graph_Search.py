import logging


class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.distance = 0
        self.visited = False

    def add_neighbor(self, v):
        if v.name not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort(key=lambda x: x.name)


class Graph:
    vertices = {}

    def add_vertex(self, v):
        if isinstance(v, Vertex):
            if v not in self.vertices.values():
                self.vertices[v.name] = v
            else:
                logging.warning("Vertex %s already present" % v.name)
        else:
            logging.warning("Not a Vertex object")

    def add_edge(self, n1, n2):
        if n1 in self.vertices and n2 in self.vertices:
            self.vertices[n1].add_neighbor(self.vertices[n2])
            self.vertices[n2].add_neighbor(self.vertices[n1])

    def bfs(self, n):
        ini_vertex = self.vertices[n]
        ini_vertex.distance = 0
        ini_vertex.visited = True
        que = [ini_vertex]

        while len(que) > 0:
            vertex = que.pop(0)
            for node in vertex.neighbors:
                if not node.visited:
                    que.append(node)
                    node.distance = vertex.distance + 1
                    node.visited = True

    def print_graph(self):
        for V in self.vertices.values():
            print(V.name+' {', end=' '),
            for neighbor in V.neighbors:
                print(neighbor.name, '', end='')
            print('}', V.distance)


G = Graph()
for ch in range(ord('A'), ord('K')):
    G.add_vertex(Vertex(chr(ch)))
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    G.add_edge(edge[0], edge[1])
G.bfs('A')
G.print_graph()
