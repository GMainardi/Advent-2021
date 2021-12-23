class Command:
    op = None
    minX = maxX = minY = maxY = minZ = maxZ = None

    def __init__(self, op, minX, maxX, minY, maxY, minZ, maxZ) -> None:
        self.op = op
        self.minX = minX
        self.maxX = maxX
        self.minY = minY
        self.maxY = maxY
        self.minZ = minZ
        self.maxZ = maxZ
    
    def get_cubes(self):
        x = range(self.minX, self.maxX+1)
        y = range(self.minY, self.maxY+1)
        z = range(self.minZ, self.maxZ+1)
        s = set()
        for dx in x:
            for dy in y:
                for dz in z:
                    s.add((dx,dy,dz))
        return s
    
    def __repr__(self) -> str:
        return f'{self.op} x={self.minX}..{self.maxX}, y={self.minY}..{self.maxY}, z={self.minZ}..{self.maxZ}'


def get_overlap(c1, c2):
    overlap = []
    for i in range(0,6,2):
        if c1[i+1] >= c2[i] and c1[i] <= c2[i+1]:
            overlap += [max(c1[i], c2[i]), min(c1[i+1], c2[i+1])]
        else:
            return None

    return tuple(overlap)


def split_cuboid(cuboid, overlap):
    new_cuboids = []
    if cuboid[0] != overlap[0]:
        new_cuboids.append((cuboid[0], overlap[0]-1, *cuboid[2:]))
    if cuboid[1] != overlap[1]:
        new_cuboids.append((overlap[1]+1, cuboid[1], *cuboid[2:]))
    if cuboid[2] != overlap[2]:
        new_cuboids.append((*overlap[:2], cuboid[2], overlap[2]-1, *cuboid[4:]))
    if cuboid[3] != overlap[3]:
        new_cuboids.append((*overlap[:2], overlap[3]+1, cuboid[3], *cuboid[4:]))
    if cuboid[4] != overlap[4]:
        new_cuboids.append((*overlap[:4], cuboid[4], overlap[4]-1))
    if cuboid[5] != overlap[5]:
        new_cuboids.append((*overlap[:4], overlap[5]+1, cuboid[5]))

    return new_cuboids

def get_volum(cuboid):
    minX, maxX, minY, maxY, minZ, maxZ = cuboid
    return (maxX-minX+1)*(maxY-minY+1)*(maxZ-minZ+1)

def count_lghts(commands):
    ons = []
    for cmd in commands:
        op = cmd.op
        cube = (cmd.minX, cmd.maxX, cmd.minY, cmd.maxY, cmd.minZ, cmd.maxZ)
        # first cube
        if len(ons) == 0:
            if op == 'on':
                ons.append(cube)
            continue
        else:
            to_remove = [] # remove cubos que vao ser cortados
            new_cubes = [cube] if op == 'on' else [] # considera o novo cubo como aceso
            for i, on_cube in enumerate(ons):
                intersec = get_overlap(on_cube, cube)
                if  intersec:
                    to_remove.append(i) # set cube to be removed
                    new_cubes += split_cuboid(on_cube, intersec) # adiciona cubos curtados
            for i in reversed(to_remove):
                del ons[i] # remove full cubes
            ons += new_cubes
    return ons

def main():
    input = [line.strip() for line in open('input.txt', 'r')]

    commands = []
    for line in input:
        op = line.split()[0]
        minX, maxX = line.split(' ')[1].split(',')[0].split('=')[1].split('..')
        minY, maxY = line.split(',')[1].split('=')[1].split('..')
        minZ, maxZ = line.split(',')[2].split('=')[1].split('..')
        c = Command(op, int(minX), int(maxX), int(minY), int(maxY), int(minZ), int(maxZ))
        commands.append(c)

    print(sum([get_volum(cuboid) for cuboid in count_lghts(commands)]))

if __name__ == '__main__':
    main()