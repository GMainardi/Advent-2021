input = [line.strip() for line in open('input_test.txt', 'r')][0]

values = input.split('=')[-1]
y = int(values.split('..')[0])
n = abs(y)-1
print(int((n+(n**2))/2))