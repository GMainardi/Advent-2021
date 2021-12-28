lanternfishes = [int(x) for x in [line.strip().split(',') for line in open('input.txt', 'r')][0]]


save = {}

def count_heir(value, days):

    if (value, days) in save:
        return save[(value, days)]
    
    if value >= days:
        return 0
    
    save[(value, days)] = 1 + count_heir(6, days-(value+1)) + count_heir(8, days-(value+1))
    return save[(value, days)]


pop = len(lanternfishes)
for fish in lanternfishes:
    pop += count_heir(fish, 256)

print(pop)