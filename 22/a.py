from itertools import permutations
import itertools

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

def run_command(command, s):
    if command.op == 'on':
        s = s.union(command.get_cubes())
    else:
        s = s.difference(command.get_cubes())
    return s

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

    s = set([])
    for command in commands:
        if command.minX >= -50 and command.maxX <= 50 and command.minY >= -50 and command.maxY <= 50 and command.minZ >= -50 and command.maxZ <= 50: 
            s = run_command(command, s)
    print(len(s))

if __name__ == '__main__':
    main()