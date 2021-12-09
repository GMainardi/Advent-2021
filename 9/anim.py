from termcolor import colored
from time import sleep
import sys

def valid(x, y, maxX, maxY):
    return x > -1 and y > -1 and x < maxX and y < maxY

def compare(x, y, matrix):
    adj = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for a, b in adj:
        if valid(a, b, len(matrix), len(matrix[0])): 
                if matrix[a][b][0] <= matrix[x][y][0]:
                    return False
    return True

def bashin(x, y, matrix):
    matrix[x][y] = (matrix[x][y][0], 3)
    F = [(x, y)]
    while len(F):
        v = F.pop(0)
        for a, b in [(v[0]-1, v[1]), (v[0]+1, v[1]), (v[0], v[1]-1), (v[0], v[1]+1)]:
            if valid(a, b, len(matrix), len(matrix[0])): 
                if matrix[a][b][1] == 0 and matrix[a][b][0] !=9:
                    matrix[a][b] = (matrix[a][b][0], 1)
                    F.append((a,b))
                    show_mat(matrix)
            

def show_mat(mat):
    string = colored('', 'white')
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y][1] == 2 or mat[x][y][1] == 3:
                string += colored(mat[x][y][0], 'red')
            elif mat[x][y][1] == 1:
                string += colored(mat[x][y][0], 'green')
            else:
               string += colored(mat[x][y][0], 'white')
        string += colored('\n', 'white')
    sys.stdout.write("\033[F"*(len(mat)+1))
    print(string)

mat = []
for line in open('anim.txt', 'r'):
    line = line.strip()
    mat.append([(int(number), 0) for number in line])

print('\n'*len(mat))

minimals = [(x,y) for x in range(len(mat)) for y in range(len(mat[0])) if compare(x, y, mat)]

for a, b in minimals:
    mat[a][b] = (mat[a][b][0], 2)

for a, b in minimals:
    bashin(a, b, mat)
