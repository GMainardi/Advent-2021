input = [line.strip() for line in open('input.txt', 'r')]

def intersec(l1, l2):
    return list(set(l1) & set(l2))

number = ['', '', '', '', '', '', '', '', '', '']

def one(list):
    for i in range(len(list)):
        if len(list[i]) == 2:
            number[1] = ''.join(sorted(list[i]))
            del list[i]
            return

def two(list):
    for i in range(len(list)):
        if len(list[i]) == 5 and len(intersec(list[i], number[6])) == 4:
            number[2] = ''.join(sorted(list[i]))
            del list[i]
            return

def three(list):
    for i in range(len(list)):
        if len(list[i]) == 5 and len(intersec(list[i], number[1])) == 2:
            number[3] = ''.join(sorted(list[i]))
            del list[i]
            return

def four(list):
    for i in range(len(list)):
        if len(list[i]) == 4:
            number[4] = ''.join(sorted(list[i]))
            del list[i]
            return

def five(list):
    for i in range(len(list)):
        if len(list[i]) == 5 and len(intersec(list[i], number[6])) == 5:
            number[5] = ''.join(sorted(list[i]))
            del list[i]
            return

def six(list):
    for i in range(len(list)):
        if len(list[i]) == 6:
            number[6] = ''.join(sorted(list[i]))
            del list[i]
            return

def seven(list):
    for i in range(len(list)):
        if len(list[i]) == 3:
            number[7] = ''.join(sorted(list[i]))
            del list[i]
            return

def eight(list):
    for i in range(len(list)):
        if len(list[i]) == 7:
            number[8] = ''.join(sorted(list[i]))
            del list[i]
            return

def nine(list):
    for i in range(len(list)):
        if len(list[i]) == 6 and len(intersec(list[i], number[3])) == 5:
                number[9] = ''.join(sorted(list[i]))
                del list[i]
                return

def zero(list):
    for i in range(len(list)):
        if len(list[i]) == 6 and len(intersec(list[i], number[9])) == 5 and len(intersec(list[i], number[1])) == 2:
            number[0] = ''.join(sorted(list[i]))
            del list[i]
            return

def decoder(list):
    # order -> one, four, seven, eight -> three -> nine -> zero -> six -> five, two
    one(list)
    four(list)
    seven(list)
    eight(list)
    three(list)
    nine(list)
    zero(list)
    six(list)
    five(list)
    two(list)


total = 0
for line in input:
    help = line.split('|')[0].split(" ")[:-1]
    decold = line.split('|')[1].split(" ")[1:]
    decoder(help)
    value = ''
    for n in decold:
        n = "".join(sorted(n))
        value += str(number.index(n))
    total += int(value)
print(total)

