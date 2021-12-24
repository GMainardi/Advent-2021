from functools import cache
class ALU:
    regs = {}

    def __init__(self) -> None:
        self.regs = {'w':0, 'x':0, 'y':0, 'z':0}

    def compute(self, op, v1, v2 = 0):
        a = self.regs[v1]
        b = self.regs[v2] if v2 in self.regs.keys() else int(v2)
        if op == 'inp':
            #print(f'{v1} <- {b}')
            self.regs[v1] = b 
        elif op == 'add':
            #print(f'{v1} <- {a} + {b}')
            self.regs[v1] = a + b
        elif op == 'mul':
            #print(f'{v1} <- {a} * {b}')
            self.regs[v1] = a * b
        elif op == 'div':
            #print(f'{v1} <- {a} // {b}')
            self.regs[v1] = a // b
        elif op == 'mod':
            #print(f'{v1} <- {a} % {b}')
            self.regs[v1] = a % b
        elif op == 'eql':
            #print(f'{v1} <- {a} == {b}')
            self.regs[v1] = int(a == b)
    
    def __repr__(self) -> str:
        return str(self.regs)

digits = ['9', '8', '7', '6', '5', '4', '3', '2', '1']

# return True if type is div z 1 else False
def block_is_1(block):
    line = block[4].split(' ')
    return int(line[2]) == 1

input = [line.strip() for line in open('input_test.txt', 'r')]
blocks = [input[i:i + 18] for i in range(0, len(input), 18)]


def run_block(block, z, digit):
    alu = ALU()
    alu.regs['z'] = z
    for line in block:
            line = line.split(' ')
            if len(line) < 3:
                alu.compute(line[0], line[1], digit)
            else:
                alu.compute(line[0], line[1], line[2])
    return alu.regs['z'], alu.regs['x']

@cache
def check_value(i=0, z=0):

    if i == len(blocks): 
        if z == 0:
            return ''
        else:
            return None

    block = blocks[i]

    for digit in digits:

        new_z, x = run_block(block, z, digit)
        
        if x != 1 or block_is_1(block):
            d = check_value(i+1, new_z)
            if d != None:
                return digit + d

    return None


print(check_value())