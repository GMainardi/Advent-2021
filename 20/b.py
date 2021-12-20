def get_adj(point):
    x, y = point
    return [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]

def show(image):
    minX, maxX = get_min_max(image, 0)
    minY, maxY = get_min_max(image, 1)
    for x in range(minX, maxX):
        for y in range(minY, maxY):
            if (x,y) in image:
                print('#', end='')
            else:print('.', end='')
        print()

def get_min_max(pixels, axis):
    sort = sorted(pixels, key=lambda x: x[axis])
    return sort[0][axis], sort[-1][axis]

def get_bin(pixels, row, col, minX, maxX, minY, maxY, it):
    bin = ""
    for x, y in get_adj((row, col)):
            if minX <= x <= maxX and minY <= y <= maxY:
                if (x, y) in pixels:
                    bin += '1'
                else:
                    bin += '0'
            elif it % 2 ==1:
                bin += '1'
            else:
                bin += '0'
    return bin

def output_image(pixels, decoding, it):
    new_pixels = set()
    minX, maxX = get_min_max(pixels, 0)
    minY, maxY = get_min_max(pixels, 1)
    for x in range(minX-1, maxX+2):
        for y in range(minY-1, maxY+2):
            bin = get_bin(pixels, x, y, minX, maxX, minY, maxY, it)
            if decoding[int(bin, 2)] == '#':
                new_pixels.add((x, y))
    return new_pixels


input = [line.strip() for line in open('input.txt', 'r')]


image_enchant = input[0]
input_image = [line for line in input[2:]]

light_pixels = set([])

for x in range(len(input_image)):
    for y in range(len(input_image)):
        if input_image[x][y] == '#':
            light_pixels.add((x,y))


for i in range(50):
    light_pixels = output_image(light_pixels, image_enchant, i)

print(len(light_pixels))
