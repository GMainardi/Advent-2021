class Tree:

    root = None

    class Node:
        left = None
        right = None
        parent = None

        def __init__(self, string) -> None:
            depth = 0
            for i, c in enumerate(string):
                if c == '[':
                    depth += 1
                if c == ']':
                    depth -= 1
                if c == ',' and depth == 1:
                    l = string[1:i]
                    r = string[i+1:-1]
                    if l.isnumeric():
                        self.left = int(l)
                    else:
                        self.left = Tree.Node(l)
                        self.left.parent = self
                    if r.isnumeric():
                        self.right = int(r)
                    else:
                        self.right = Tree.Node(r)
                        self.right.parent = self
        

        def __repr__(self) -> str:
            return f'[{str(self.left)},{str(self.right)}]'
        
    def __init__(self, string='') -> None:
        self.root = Tree.Node(string)       

    def __repr__(self) -> str:
        return str(self.root)
    
    def __add__(self, other) -> None:
        tree = Tree()
        tree.root.left = Tree.Node(str(self))
        tree.root.right = Tree.Node(str(other))
        tree.root.left.parent = tree.root.right.parent = tree.root
        #simplify
        while tree.explodes(tree.root) or tree.split():
            pass
        return tree

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
    
    def up_left(self, curr, value):
        if curr.parent:
            if curr.parent.left == curr:
                self.up_left(curr.parent, value)
            else:
                if type(curr.parent.left) == int:
                    curr.parent.left += value
                else:
                    self.down_right(curr.parent.left, value)
    

    def down_right(self, curr, value):
        if type(curr.right) == Tree.Node:
            self.down_right(curr.right, value)
        else:
            curr.right += value
    
    def up_right(self, curr, value):
        if curr.parent:
            if curr.parent.right == curr:
                self.up_right(curr.parent, value)
            else:
                if type(curr.parent.right) == int:
                    curr.parent.right += value
                else:
                    self.down_left(curr.parent.right, value)
    
    def down_left(self, curr, value):
        if type(curr.left) == Tree.Node:
            self.down_left(curr.left, value)
        else:
            curr.left += value

    def explodes(self, curr, depth = 1):
        if type(curr) == Tree.Node:
            if depth == 5:
                self.up_right(curr, curr.right)
                self.up_left(curr, curr.left)
                if curr.parent.left == curr:
                    curr.parent.left = 0
                elif curr.parent.right == curr:
                    curr.parent.right = 0
                return True
            return self.explodes(curr.left, depth + 1) or self.explodes(curr.right, depth + 1)
        return False
        
    def get_numb(self, string, index):
        ans = ''
        while string[index].isnumeric():
            ans += string[index]
            index +=1
        return int(ans), index

    def split(self):
        tree = str(self)
        i = 0
        while i < len(tree)-1:

            if tree[i].isnumeric() and tree[i+1].isnumeric():
                numb, index = self.get_numb(tree, i)
                l = numb // 2
                r = numb - l
                tree = tree[:i] + f'[{l},{r}]' + tree[index:]
                self.root = Tree.Node(tree)
                return True
            i += 1
        return False

    def magnitude(self, curr):
        if type(curr) == int:
            return curr
        else:
            return 3*self.magnitude(curr.left) + 2*self.magnitude(curr.right)



input = [Tree(line.strip()) for line in open('input.txt', 'r')]
ans = sum(input)
print(ans.magnitude(ans.root))