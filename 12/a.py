class Graph:
    
    nodes = []

    class Node:
        def __init__(self, name) -> None:
            self.name = name
            self.neighbours = []
        
        def add_neighbour(self, n):
            self.neighbours.append(n)

        def show(self):
            n = [x.name for x in self.neighbours]
            print(f'{self.name} : {n}')

        def is_big_cave(self):
            return self.name.upper() == self.name

    def __init__(self) -> None:
        self.nodes = []
    
    def add(self, n1, n2):

        n_1 = self.in_graph(n1)
        n_2 = self.in_graph(n2)

        if n_1:
            n1 = n_1
        else:
            self.nodes.append(n1)
        if n_2:
            n2 = n_2
        else:
            self.nodes.append(n2)

        n1.add_neighbour(n2)
        n2.add_neighbour(n1)
        
    def show(self):
        for node in self.nodes:
            node.show()

    def in_graph(self, n : Node):
        for node in self.nodes:
            if node.name == n.name:
                return node
        return False
    
    def find_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None

def create_graph(input):
    g = Graph()
    for line in input:
        n1, n2 = line.split('-')
        n1 = Graph.Node(n1)
        n2 = Graph.Node(n2)
        g.add(n1, n2)
    return g

def path(curr : Graph.Node, dest : Graph.Node, marks):

    if not curr.is_big_cave():
        marks[curr.name] = 1

    if curr.name == dest.name:
        return 1
    
    total = 0
    for neig in curr.neighbours:
        if not marks[neig.name]:
            total += path(neig, dest, marks.copy())
    return total
    

input = [line.strip() for line in open('input.txt', 'r')]

g = create_graph(input)
g.show()

marked = {k.name:0 for k in g.nodes}

print(path(g.find_node('start'), g.find_node('end'), marked))