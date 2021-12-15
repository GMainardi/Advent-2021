from dijkstar import Graph, find_path

g = Graph()
nodes = {}

def valid(x, y, maxX, maxY):
    return x > -1 and y > -1 and x < maxX and y < maxY
    
mat = []
for line in open('input.txt', 'r'):
    line = line.strip()
    mat.append([int(number) for number in line])
    
i = 0
for x in range(len(mat)):
    for y in range(len(mat[0])):
        nodes[(x, y)] = i
        i += 1

for x in range(len(mat)):
    for y in range(len(mat[0])):
        for x1, y1 in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if valid(x1, y1, len(mat), len(mat[0])):
                g.add_edge(nodes[(x, y)], nodes[(x1, y1)], mat[x1][y1])


print(find_path(g, 0, i-1).total_cost)