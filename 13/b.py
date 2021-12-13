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

def to_mat(dots):
    a, b = max(dots)
    mat = []
    for x in range(a):
        mat.append('')
        for y in range(b):
            if (x, y) in dots:
                mat[x] += '#'
            else:
                mat[x] += '.'
    return mat

def split_letters(mat):
    letters = []
    start = 0
    end = 4
    while end <= len(mat[0]):
        letter = ''
        for line in range(len(mat)):
            letter += mat[line][start:end]
        letters.append(letter)
        start += 5
        end += 5
    return letters

def get_alpha(f):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    start = 0
    letters = {}
    for i in range(26):
        letter = ''.join(f[start:start+6])
        letters[letter] = alpha[i]
        start += 7
    return letters

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

f = [line.strip() for line in open('letters.txt')]

show(dots)

out = split_letters(to_mat(dots))
gab = get_alpha(f)

for letter in out:
    print(gab[letter], end='')