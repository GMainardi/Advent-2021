input = [line.strip() for line in open('input.txt', 'r')]

count = 0
known_len = [2, 3, 4, 7]
for line in input:
    line = line.split('|')[1].split(" ")
    for numb in line:
        if len(numb) in known_len:
            count += 1

print(count)