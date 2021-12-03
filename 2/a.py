input = [(line.strip().split(' ')[0], int(line.strip().split(' ')[1])) for line in open('input.txt', 'r')]

pos = (0,0)

for command, value in input:
    if command == 'forward':
        pos = (pos[0]+value, pos[1])
    elif command == 'down':
        pos = (pos[0], pos[1]+value)
    elif command == 'up':
        pos = (pos[0], pos[1]-value)
    else:
        print('nao deveria estar aqui')

print(pos[0]*pos[1])