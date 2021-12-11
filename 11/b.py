import numpy as np

def add(mat1, mat2):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            mat1[x][y] += int(mat2[x][y])


def valid(x, y, maxX, maxY):
    return x > -1 and y > -1 and x < maxX and y < maxY


def flash(x, y, mat):
    temp = np.zeros((len(mat), len(mat[0])))
    adj = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    for a, b in adj:
        if valid(a, b, len(mat), len(mat[0])): 
                temp[a][b] +=1
    return temp


def increase(mat):
    new = np.zeros((len(mat), len(mat[0])))
    flashes = np.zeros((len(mat), len(mat[0])))
    flashed = False
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            mat[x][y] += 1
            if mat[x][y] > 9 and flashes[x][y] == 0:
                flashes[x][y] = 1
                flashed = True
                add(new,flash(x, y, mat))
    add(mat, new)
    if flashed:
        check(mat, flashes)
    return clean_mat(mat)


def check(mat, flashes):
    new = np.zeros((len(mat), len(mat[0])))
    flashed = False
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] > 9 and flashes[x][y] == 0:
                flashes[x][y] = 1
                flashed = True
                add(new,flash(x, y, mat))
    add(mat, new)
    if flashed:
        check(mat, flashes)


def clean_mat(mat):
    f = 0
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[x][y] > 9:
                f += 1
                mat[x][y] = 0
    return f == len(mat) * len(mat[0])


def show_mat(mat):
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            print(mat[x][y], end='')
        print()


input =  [line.strip() for line in open('input.txt', 'r')]

mat = []
for line in input:
    mat.append([int(value) for value in line])

i = 0
while not increase(mat):
    i += 1
print(i+1)