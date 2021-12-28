import numpy as np

def next(a, b):
    if a > b:
        return a-1
    elif a < b:
        return a + 1
    return a

def create_path(matrix, x1, x2, y1, y2):
    matrix[x1][y1] += 1

    if x1 == x2 and y1 == y2:
        return

    x1 = next(x1, x2)
    y1 = next(y1, y2)
    create_path(matrix, x1, x2, y1, y2)


input = [line.strip().replace(" -> ", ",") for line in open('input.txt', 'r')]

matrix = np.zeros((1000,1000))

for line in input:
    line = [int(x) for x in line.split(",")]
    create_path(matrix, line[0], line[2], line[1], line[3])

count = 0
for x in range(len(matrix)):
  for y in range(len(matrix)):
    if matrix[x][y] > 1:
      count += 1
print(count)