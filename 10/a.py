input = [line.strip() for line in open('input.txt', 'r')]

def error_line(line):

    stack = []
    open = '([{<'
    close = ')]}>'

    for elem in line:
        if elem in open:
            stack.append(elem)
        if elem in close:
            if stack[-1] == '(':
                if elem == ')':
                    stack.pop(-1)
                else:
                    #print('expected ), but found {elem} instead.')
                    return elem
            elif stack[-1] == '[':
                if elem == ']':
                    stack.pop(-1)
                else:
                    #print(f'expected ], but found {elem} instead.')
                    return elem
            elif stack[-1] == '{':
                if elem == '}':
                    stack.pop(-1)
                else:
                    #print('expected }',f', but found {elem} instead.')
                    return elem
            elif stack[-1] == '<':
                if elem == '>':
                    stack.pop(-1)
                else:
                    #print(f'expected >, but found {elem} instead.')
                    return elem
    return False

cost = {')':3, ']': 57, '}':1197, '>':25137}
total = 0

for line in input:
    error_char = error_line(line)
    if error_char:
        total += cost[error_char]

print(total)
