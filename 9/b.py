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

def bashin(x, y, matrix):

    if matrix[x][y] == 9:
        return 0

    sum = 1
    for a, b in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if valid(a, b, len(matrix), len(matrix[0])):
            matrix[x][y] = 9
            sum += bashin(a, b, matrix)
    return sum

mat = []
for line in open('input.txt', 'r'):
    line = line.strip()
    mat.append([int(number) for number in line])


maxes = [0, 0, 0]
for x in range(len(mat)):
    for y in range(len(mat[0])):
        if compare(x, y, mat):
            tam = bashin(x, y, mat)
            if tam > min(maxes):
                maxes[maxes.index(min(maxes))] = tam

risk = 1               
for val in maxes:
    risk *= val
print(risk)