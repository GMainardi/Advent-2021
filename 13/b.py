def first_parse(line):
    a, b = line.split(',')
    return int(b), int(a)

def second_parse(line):
    ax, value = line.split(' ')[2].split('=')
    return ax, int(value)

def fold(dots, axis, value):
    if axis == 'y':
        top = set(filter(lambda x : x[0] < value, dots))
        bot = dots - top
        bot = set(map(lambda x : (value - (x[0] - value), x[1]), bot))
    else:
        top = set(filter(lambda x : x[1] < value, dots))
        bot = dots - top
        bot = set(map(lambda x : (x[0], value - (x[1] - value)), bot))
    
    return bot.union(top)

def max(dots):
    maxX = 0
    maxY = 0
    for x, y in dots:
        if maxX < x:
            maxX = x
        if maxY < y:
            maxY = y
    return maxX+1, maxY+1

def show(dots):
    a, b = max(dots)
    for x in range(a):
        for y in range(b):
            if (x, y) in dots:
                print('#', end = '')
            else:
                print('.', end = '')
        print()
    print()

input = [line.strip() for line in open('input.txt', 'r')]

first = True
dots = set()
folds = []
for line in input:
    if first:
        if line == '':
            first = False
        else:
            dots.add(first_parse(line))
    else:
        folds.append(second_parse(line))

for f in folds:
    dots = fold(dots, f[0], f[1])

show(dots)