def show(set):
    for x in range(max_x):
        for y in range(max_y):
            if (x,y) in set:
                print(directions[(x,y)], end='')
            else:
                print('.', end='')
        print()

def get_next_side(cucuber, set):
    x, y = cucuber
    y += 1
    if y == max_y: y = 0
    if (x,y) in set: return False
    else: return (x,y)
    
def get_next_down(cucuber, set):
    x, y = cucuber
    x += 1
    if x == max_x: x = 0
    if (x,y) in set: return False
    else: return (x,y)
       
def move_side(set):
    new_set = set.copy()
    for cucuber in set:
        if directions[cucuber] == '>':
            new_pos = get_next_side(cucuber, set)
            if new_pos:
                new_set.remove(cucuber)
                del directions[cucuber]
                new_set.add(new_pos)
                directions[new_pos] = '>'
            else:
                continue
    return new_set

def move_down(set):
    new_set = set.copy()
    for cucuber in set:
        if directions[cucuber] == 'v':
            new_pos = get_next_down(cucuber, set)
            if new_pos:
                new_set.remove(cucuber)
                del directions[cucuber]
                new_set.add(new_pos)
                directions[new_pos] = 'v'
            else:
                continue
    return new_set

def move(set):
    set = move_side(set)
    return move_down(set)
    

input = [line.strip() for line in open('input.txt', 'r')]

max_y = len(input[0])
max_x = len(input)

sea_cucumbers = set([])
directions = {}
for x in range(max_x):
    for y in range(max_y):
        if input[x][y] == '>':
            sea_cucumbers.add((x, y))
            directions[(x,y)] = '>'
        elif input[x][y] == 'v':
            sea_cucumbers.add((x, y))
            directions[(x,y)] = 'v'


old = sea_cucumbers.copy()
sea_cucumbers = move(sea_cucumbers)
i = 1
while len(old.difference(sea_cucumbers)):
    old = sea_cucumbers.copy()
    #print(f'--- step {i} ---')
    sea_cucumbers = move(sea_cucumbers)
    #show(sea_cucumbers)
    #print()
    i += 1

print(i)