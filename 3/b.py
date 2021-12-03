input = [line.strip() for line in open('input.txt', 'r')]

def mode(arr, gt):
    ones = 0
    zeros = 0
    for e in arr:
        if e == '1':
            ones +=1
        else:
            zeros += 1
    return str(int(ones >= zeros)) if gt else str(int(ones < zeros))

def oxigen_rat(arr, i=0):

    if len(arr) == 1:
        return to_int(arr[0])

    cut = mode([b[i] for b in arr], 1)
    return oxigen_rat([elem for elem in arr if elem[i] == cut], i+1)

def CO2(arr, i=0):

    if len(arr) == 1:
        return to_int(arr[0])

    cut = mode([b[i] for b in arr], 0)
    return CO2([elem for elem in arr if elem[i] == cut], i+1)

def to_int(value):
    return int(''.join(value), 2)

print(oxigen_rat(input) * CO2(input))
