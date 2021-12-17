from math import floor, ceil, sqrt
import time
def reverse_gauss(value):
    delt = abs(1-(-8*value))
    ans = (-1 + sqrt(delt))/2
    return ans

def it_dict(y):
    arr = {}
    for it in range(2*y+2):
        arr[it] = []
    return arr

input = [line.strip() for line in open('input_test.txt', 'r')][0]

values = input.split(' ')[2:]
x1, x2 = values[0].replace(',', '').split('=')[1].split('..')
y2, y1 = values[1].replace(',', '').split('=')[1].split('..')

start = (int(x1), int(y1))
end = (int(x2), int(y2))
hits = 0
minx = ceil(reverse_gauss(int(x1)))
st = time.time()
hits_x = it_dict(abs(end[0]))
for x in range(minx, end[0]+1):
    hit = (x + x**2)/2

    if hit <= end[0]:
        temp = hit - start[0]
        it = x - floor(reverse_gauss(temp))
        for i in range(it, len(hits_x.keys())):
            hits_x[i].append(x)

    else:
        temp = hit - start[0]
        first_hit = x - floor(reverse_gauss(temp))
        last_hit = x - ceil(reverse_gauss(hit-end[0]))
        if last_hit == first_hit:
            hits_x[last_hit].append(x)
        else:
            for i in range(first_hit, last_hit+1):
                hits_x[i].append(x)
 
points = set([])
for y in range(end[1],abs(end[1])):
    if y > 0:
        max = int((y+(y**2))/2)
        s = max - start[1]
        e = max - end[1]
        first_hit = (y+1) + ceil(reverse_gauss(s))
        last_hit = (y+1) + floor(reverse_gauss(e))
        if first_hit == last_hit:
            for x in hits_x[first_hit]:
                points.add((x,y))
        else:
            for i in range(first_hit, last_hit+1):
                for x in hits_x[i]:
                    points.add((x,y))
    else:
        pos = 0
        vel = y
        it = 0
        if y > 0:
            it += y*2 + 1
            vel = (y+1) * -1
        while pos >= end[1]:
                if pos <= start[1]:
                    for x in hits_x[it]:
                        points.add((x,y))
                pos += vel
                vel -= 1
                it += 1
et = time.time()
print(et-st)
print(len(points))
