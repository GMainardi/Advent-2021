from typing import Counter


def step(tamplate, rules, tam=2):
    start = 0
    new = ''
    while start + tam < len(template):
        new += rules[tamplate[start:start+2]][:-1]
        start += 1
    new += rules[tamplate[start:start+2]]
    return new

input = [line.strip() for line in open('input.txt', 'r')]


rules = {}
template = input[0]
for i in range(2, len(input)):
    pre, pos = input[i].split(' -> ')
    rules[pre] = pre[0] + pos + pre[1]

for i in range(10):
    template = step(template, rules)

mc = Counter(template).most_common()[0][1]
lc = Counter(template).most_common()[-1][1]

print(mc - lc)
print(len(template))