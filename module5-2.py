class No:
    __height = 0
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = No(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = No(data)

def height(tree):
    if not tree:
        return 0
    return max(height(tree.left), height(tree.right))+1

def checking(tree):
        if tree.left and tree.right:
            if abs(height(tree.right) - height(tree.left)) > 1:
                return False
        else:
            if not tree.right and tree.left and height(tree.left) > 1:
                return False 
            if not tree.left and tree.right and height(tree.right) > 1:
                return False
        if tree.left:
            if not check_tree(tree.left):
                return False
        if tree.right:    
            if not check_tree(tree.right):
                return Fasle

def build_tree(elements):
    tree = No(elements[0])
    for i in range(1, len(elements)):
        tree.add(elements[i])
    return tree


def main():
    elements = list(map(int, input().split()))
    tree = build_tree(elements[:len(elements)])
    print("NO") if checking(tree) else print("YES")
main()