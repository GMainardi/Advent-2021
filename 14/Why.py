def sum_frecs(f1 : dict, f2: dict):
    temp = {}
    keys = list(set(f1.keys()).union(set(f2.keys())))
    for k in keys:
        temp[k] = f1.get(k, 0) + f2.get(k, 0)
    return temp

def get_pairs(template):
    start = 0
    ans = []
    while start+1 < len(template):
        ans.append(template[start:start+2])
        start += 1
    return ans

mem = {}

def count(pair, steps=39):

    if pair in mem.keys():
        if steps in mem[pair].keys():
            return mem[pair][steps]

    left, right = rules[pair]
    frecs = {left[1]: 1}

    if not steps:
        if pair not in mem.keys():
            mem[pair] = {}
        mem[pair][steps] = frecs
        return frecs
    
    mem[left][steps-1] = count(left, steps-1)
    mem[right][steps-1] = count(right, steps-1)

    frecs = sum_frecs(mem[left][steps-1], mem[right][steps-1])
    frecs[left[1]] = frecs.get(left[1], 0) + 1

    if pair not in mem.keys():
        mem[pair] = {}
    mem[pair][steps] = frecs

    return mem[pair][steps]


input = [line.strip() for line in open('input.txt', 'r')]

rules = {}
template = input[0]

for i in range(2, len(input)):
    pre, pos = input[i].split(' -> ')
    rules[pre] = (pre[0] + pos, pos + pre[1])

pairs = get_pairs(template)

for pair in pairs:
    mem[pair] = {}

frecs = {}

for letter in template:
    frecs[letter] = frecs.get(letter, 0) + 1

for pair in pairs:
    frecs = sum_frecs(frecs, count(pair))

most = max([x[1] for x in frecs.items()])
lest = min([x[1] for x in frecs.items()])

print(most - lest)