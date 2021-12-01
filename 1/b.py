input = [int(line.strip()) for line in open('input.txt', 'r')]

start = 0
end = 3
incs = 0

while end < len(input):
    prev = sum(input[start:end])
    curr = sum(input[start+1:end+1])
    if  prev < curr:
        incs +=1
    start += 1
    end += 1


print(incs)