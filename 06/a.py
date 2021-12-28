lanternfishes = [int(x) for x in [line.strip().split(',') for line in open('input.txt', 'r')][0]]


def decrese_day(arr):
    to_increse = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 6
            to_increse +=1
        else:
            arr[i] -= 1
    for _ in range(to_increse):
        arr.append(8)

for i in range(256):
    decrese_day(lanternfishes)

print(len(lanternfishes))