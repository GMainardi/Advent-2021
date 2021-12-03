input = [line.strip() for line in open('input.txt', 'r')]

def Gamma(arr):
    count_ones = []
    for binary in arr:
        for index, bit in enumerate(binary):
            if len(count_ones)-1 < index:
                count_ones.append(bit == '1')
            else:
                count_ones[index] += bit == '1'

    gamma = list(map(lambda x : str(int(x > len(arr)/2)), count_ones))
    return gamma

def Epslon(gamma):
    return [ str(int(bit == '0')) for bit in gamma]


def to_int(value):
    return int(''.join(value), 2)


gamma = Gamma(input)
epslon = Epslon(gamma)
gamma_10 = to_int(gamma)
epslon_10 = to_int(epslon)

print(gamma_10 * epslon_10)
