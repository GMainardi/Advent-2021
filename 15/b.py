from dijkstar import Graph, find_path

def valid(x, y, maxX, maxY):
    return x > -1 and y > -1 and x < maxX and y < maxY

def increse(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] == 9:
                mat[x][y] = 1
            else:
                mat[x][y] += 1
    return mat

def show(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            print(mat[x][y], end ='')
        print()

mat = []
for line in open('input.txt', 'r'):
    line = line.strip()
    mat.append([int(number) for number in line])

g = Graph()
nodes = {}

print()
inc_mat = [line.copy() for line in mat]

for x in range(4):
    inc_mat = increse(inc_mat)
    for line in range(len(mat)):
        mat[line] = [*mat[line], *inc_mat[line]]

inc_mat = [line.copy() for line in mat]

for x in range(4):
    inc_mat = increse([line.copy() for line in inc_mat])
    mat.extend(inc_mat)

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