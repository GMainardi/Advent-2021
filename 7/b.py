input = [int(x)  for x in [line.split(',') for line in open('input.txt', 'r')][0]]


def fuel_cost(value, arr):
    total = 0
    for pos in arr:
        n = abs(pos-value)
        total += (n*(n+1))//2
    return total

min = fuel_cost(input[0], input)

for i in range(max(input)):
    cost = fuel_cost(i, input)
    if cost < min:
        min = cost

print(min)