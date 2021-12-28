input = [int(line.strip()) for line in open('input.txt', 'r')]

prev = input[0]
incs = 0
for mesure in input:
    if mesure > prev:
        incs += 1
    prev = mesure

print(incs)