from heapq import heappop, heappush
class Graph:
    nodes = {}

    class Vertex:
        def __init__(self, n1, n2, weight) -> None:
            self.n1 = n1
            self.n2 = n2
            self.weight = weight
        
        def get_other(self, node):
            return self.n1 if node == self.n2 else self.n2
        
        def __repr__(self):
            return f'({self.n1}, {self.n2}, {self.weight})'

    def __init__(self, mat) -> None:
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                for x1, y1 in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if valid(x1, y1, len(mat), len(mat[0])):
                        self.add_edge((x, y), (x1, y1), mat[x1][y1])
    
    def add_edge(self, n1, n2, weight):
        if n1 not in self.nodes.keys():
            self.nodes[n1] = []
        if n2 not in self.nodes.keys():
            self.nodes[n2] = []
        vertex = self.Vertex(n1, n2, weight)
        self.nodes[n1].append(vertex)

def find_path(g : Graph, init):
    dist = {}
    prev = {}
    dist[init] = 0

    Q = []

    for k in g.nodes.keys():
        if k != init:
            dist[k] = float('inf')
            prev[k] = None
    
    heappush(Q, (dist[init], init))

    while len(Q):
        curr = heappop(Q)[1]
        for vertex in g.nodes[curr]:
            nxt = vertex.get_other(curr)
            new_value = dist[curr] + vertex.weight
            if new_value < dist[nxt]:
                dist[nxt] = new_value
                prev[nxt] = curr
                heappush(Q, (new_value, nxt))
    
    return dist

def valid(x, y, maxX, maxY):
    return x > -1 and y > -1 and x < maxX and y < maxY
    
mat = []
for line in open('input.txt', 'r'):
    line = line.strip()
    mat.append([int(number) for number in line])
    
g = Graph(mat)

last = ((len(mat)-1), len(mat[0])-1)

dist = find_path(g, (0, 0))[last]

print(dist)