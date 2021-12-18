class Tree:

    # build Tree
    def __init__(self, string =''):
        depth = 0
        self.left = self.right = self.parent = None
        for i,c in enumerate(string[1:-1]):
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
            elif c == ',' and depth == 0:
                self.left = Tree(string[1:i+1])
                self.right = Tree(string[i+2:-1])
                self.left.parent = self.right.parent = self
        # cast to int 
        self.value = int(string) if string.isnumeric() and not self.left else None
    
    def  __repr__(self):
        #to String
        if not self.left: 
            return str(self.value)
        else: 
            return "[" + str(self.left) + "," + str(self.right) + "]"

    def __add__(self, other):
        tree = Tree()
        tree.left = Tree(str(self))
        tree.right = Tree(str(other))
        tree.left.parent = tree.right.parent = tree
        # simplify
        while tree.explode(0) or tree.split():
            pass
        return tree

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
    
    def explode_to_left(self):

        curr = self.parent
        old = self

        # while i'm comming from left
        while curr and curr.left == old:
            old = curr
            curr = curr.parent
        
        if curr:
            curr = curr.left

        # go to right
        while curr and curr.right:
            curr = curr.right
        
        return curr
    
    def explode_to_right(self):
        curr = self.parent
        old = self
        while curr and curr.right == old:
            old = curr
            curr = curr.parent
        
        if curr:
            curr = curr.right
        
        while curr and curr.left:
            curr = curr.left

        return curr

    def explode(self, depth):
            if self.left:
                if depth == 4 and not self.left.left and not self.right.left:

                    left = self.explode_to_left()
                    right = self.explode_to_right()

                    if left:
                        left.value += self.left.value
                    
                    if right:
                        right.value += self.right.value
                    
                    self.left = None
                    self.right = None
                    self.value = 0

                    return True
                return self.left.explode(depth+1) or self.right.explode(depth+1)
            return False
    
    def split(self):
        if self.value and self.value > 9:
            l = self.value // 2
            r = self.value - l
            self.left = Tree(str(l))
            self.right = Tree(str(r))
            self.left.parent = self.right.parent = self
            self.value = None
            return True
        if self.left:
            return self.left.split() or self.right.split()
        return False
    
    def magnitude(self):
        if self.left:
            return 3*self.left.magnitude() + 2*self.right.magnitude()
        return int(self.value)

trees = [Tree(line.strip()) for line in open('input.txt', 'r')]
max_mag = 0
for t1 in trees:
    for t2 in trees:
        if t1 != t2:
            curr = t1 + t2
            if curr.magnitude() > max_mag:
                max_mag = curr.magnitude()
print(max_mag)