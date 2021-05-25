class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def add(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)

def height(tree):
    if not tree:
        return 0
    return max(height(tree.left), height(tree.right))+1

def is_balanced(tree):
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and is_balanced(tree.left) and is_balanced(tree.right)):
        return True # лучше так
    return False

def build_tree(elements):
    tree = Node(elements[0])
    for i in range(1, len(elements)-1):
        tree.add(elements[i])
    return tree

def main():
    list_ = list(map(int, input().split()))
    tree = build_tree(list_)
    if is_balanced(tree):
        print("YES")
    else:
        print("NO")
main()