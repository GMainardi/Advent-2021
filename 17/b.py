from math import ceil, sqrt
def shot(pos, vel):
    pos = (pos[0] + vel[0], pos[1] + vel[1])
    if vel[0] != 0:
        vel = (vel[0] + 1 if vel[0] < 0 else vel[0] -1, vel[1]-1)
    else:
        vel = (vel[0], vel[1]-1)
    return pos, vel

def hit(pos, start, end):
    return (pos[0] >= start[0] and pos[0] <= end[0]) and (pos[1] <= start[1] and pos[1] >= end[1])

def can_hit(pos, end):
    return pos[0] <= end[0] and pos[1] >= end[1]

input = [line.strip() for line in open('input.txt', 'r')][0]

values = input.split(' ')[2:]
x1, x2 = values[0].replace(',', '').split('=')[1].split('..')
y2, y1 = values[1].replace(',', '').split('=')[1].split('..')

start = (int(x1), int(y1))
end = (int(x2), int(y2))
hits = 0
delt = sqrt(abs(1-(8*int(x1))))
minx = ceil((1 + delt)/2)
for x in range(minx-1, end[0]+1):
    for y in range(end[1],abs(end[1])):
        pos = (0,0)
        vel = (x, y)
        my = 0
        while can_hit(pos, end) and not hit(pos, start, end):
            pos, vel = shot(pos, vel)
        if hit(pos, start, end):
            hits += 1
print(hits)