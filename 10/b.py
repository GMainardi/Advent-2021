import statistics

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
                    return True, None
            elif stack[-1] == '[':
                if elem == ']':
                    stack.pop(-1)
                else:
                    #print(f'expected ], but found {elem} instead.')
                    return True, None
            elif stack[-1] == '{':
                if elem == '}':
                    stack.pop(-1)
                else:
                    #print('expected }',f', but found {elem} instead.')
                    return True, None
            elif stack[-1] == '<':
                if elem == '>':
                    stack.pop(-1)
                else:
                    #print(f'expected >, but found {elem} instead.')
                    return True, None
    return False, stack

def complete_command(stack):
    missing = ''
    while len(stack):
        top = stack.pop(-1)
        if top == '(':
            missing += ')'
        if top == '[':
            missing += ']'
        if top == '{':
            missing += '}'
        if top == '<':
            missing += '>'
    return missing


cost = {')':1, ']': 2, '}':3, '>':4}
total = []

for line in input:
    err, stack = error_line(line)
    if not err:
        missing = complete_command(stack)
        sub_total = 0
        for char in missing:
            sub_total *=5
            sub_total += cost[char]
        total.append(sub_total)

print(statistics.median(total))