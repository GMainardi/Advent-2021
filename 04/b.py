def read_input():
    arq = open('input.txt', 'r')
    cartelas = []
    cartela = []
    for index, line in enumerate(arq):
        line = line.strip()
        if index == 0:
            numbers = list(map(lambda x : int(x), line.split(',')))
        
        else:
            if len(line):
                cartela.append(list(map(lambda x : (int(x), 0), line.replace("  ", " ").split(' '))))
            else:
                if len(cartela):
                    cartelas.append(cartela)
                    cartela = []
    cartelas.append(cartela)
    return numbers, cartelas    

def check_value(number, cartelas):
    for cartela in cartelas:
        for row in cartela:
            for index, tuple in enumerate(row):
                if tuple[0] == number:
                    row[index] = (tuple[0], 1)

def print_cartelas(cartelas):
    for cartela in cartelas:
        for row in cartela:
            print(row)
        print()

def row_bingo(cartela):
    for row in cartela:
        if all([x[1] for x in row]):
            return True
    return False

def column_bingo(cartela):
    for i in range(len(cartela)):
        if all([row[i][1] for row in cartela]):
            return True
    return False

def bingo(cartela):
    return row_bingo(cartela) or column_bingo(cartela)

def sum_unmarked(cartela):
    sum = 0
    for row in cartela:
        for elem, c in row:
            if c == 0:
                sum += elem
    return sum

numbers, cartelas = read_input()

for number in numbers:
    check_value(number, cartelas)
    k = 0
    while k < len(cartelas):
        if bingo(cartelas[k]):
            if len(cartelas) == 1:
                print_cartelas(cartelas)
                soma = sum_unmarked(cartelas[0])
                print(number*soma)
                exit(0)

            del cartelas[k]
        else:
            k += 1
        