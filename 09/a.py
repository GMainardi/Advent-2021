from termcolor import colored

def valid(x, y, maxX, maxY):
    return x > -1 and y > -1 and x < maxX and y < maxY

def compare(x, y, matrix):
    adj = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for a, b in adj:
        if valid(a, b, len(matrix), len(matrix[0])): 
                if matrix[a][b] <= matrix[x][y]:
                    return False
    return True

def show_mat(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if compare(x, y, mat):
                print(colored(mat[x][y], 'red'), end='')
            else:
                print(colored(mat[x][y], 'white'), end='')
        print()

mat = []
for line in open('input.txt', 'r'):
    line = line.strip()
    mat.append([int(number) for number in line])

#show_mat(mat)

risk = 0
for x in range(len(mat)):
    for y in range(len(mat[0])):
        if compare(x, y, mat):
            risk += (1 + mat[x][y])
print()
print(risk)