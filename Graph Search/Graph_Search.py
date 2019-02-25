import logging


class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.distance = 0
        self.color = 'black'

    def add_neighbor(self, V):
        if V.name not in self.neighbors:
            self.neighbors.append(V)
            self.neighbors.sort(key=lambda x: x.name)


class Graph:
    vertices = {}

    def add_vertex(self, V):
        if isinstance(V, Vertex):
            if V not in self.vertices.values():
                self.vertices[V.name] = V
            else:
                logging.warning("Vertex %s already present" %V.name)
        else:
            logging.warning("Not a Vertex object")

    def add_edge(self, n1, n2):
        if n1 in self.vertices and n2 in self.vertices:
            self.vertices[n1].add_neighbor(self.vertices[n2])
            self.vertices[n2].add_neighbor(self.vertices[n1])
            # for n, V in self.vertices:
            #     if n == n1:
            #         V.add_neighbor(self.vertices[n2])
            #     if n == n2:
            #         V.add_neighbor(self.vertices[n2])

    def bfs(self, n):
        ini_vertex = self.vertices[n]
        ini_vertex.distance = 0
        ini_vertex.color = 'red'
        que = [ini_vertex]

        while len(que) > 0:
            vertex = que.pop(0)
            for node in vertex.neighbors:
                if node.color != 'red':
                    que.append(node)
                    node.distance = vertex.distance + 1
                    node.color = 'red'

    def print_graph(self):
        for V in self.vertices.values():
            print(V.name+' {', end=' '),
            for neighbor in V.neighbors:
                print(neighbor.name,'', end=''),
            print('}', V.distance)


G = Graph()
for ch in range(ord('A'), ord('K')):
    G.add_vertex(Vertex(chr(ch)))
edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    G.add_edge(edge[0],edge[1])
G.bfs('A')
G.print_graph()





