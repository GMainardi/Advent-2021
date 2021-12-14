def get_pairs(template):
    start = 0
    ans = []
    while start+1 < len(template):
        ans.append(template[start:start+2])
        start += 1
    return ans

def step(pairs_frequencies : dict, rules : dict, frequencies : dict):

    temp = {}
    for k, v in pairs_frequencies.items():

        left, right = rules[k]
        frequencies[left[1]] = frequencies.get(left[1], 0) + v
        temp[left] = temp.get(left, 0) + v
        temp[right] = temp.get(right, 0) + v

    return temp

input = [line.strip() for line in open('input.txt', 'r')]

rules = {}
template = input[0]
for i in range(2, len(input)):
    pre, pos = input[i].split(' -> ')
    rules[pre] = (pre[0] + pos, pos + pre[1])

pairs_frequencies = {}
frequencies = {}

for l in template:
    frequencies[l] = frequencies.get(l, 0) + 1

for pair in get_pairs(template):
    pairs_frequencies[pair] = pairs_frequencies.get(pair, 0) + 1


for i in range(40):
    pairs_frequencies = step(pairs_frequencies, rules, frequencies)

most = max([x[1] for x in frequencies.items()])
lest = min([x[1] for x in frequencies.items()])

print(most - lest)