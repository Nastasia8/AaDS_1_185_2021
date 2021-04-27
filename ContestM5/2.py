

class Node:
    __size = 0
    __height = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.__size += 1

    @property
    def size(self):
        return self.__size

    @property
    def height(self):
        return self.__height

    def add(self, value, depth):
        if self.data == value:
            return

        if value < self.data:
            if self.left:
                self.left.add(value, depth+1)
            else:
                if Node.__height < depth:
                    Node.__height = depth
                self.left = Node(value)

        else:
            if self.right:
                self.right.add(value, depth+1)
            else:
                if Node.__height < depth:
                    Node.__height = depth
                self.right = Node(value)

#Questionable
def height(tree):
    if not tree:
        return 0
    return (max(height(tree.left), height(tree.right))+1)

def is_balanced(tree):
    if height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1:
        return "YES"
    return "NO"

def build_tree(elements):
    tree = Node(elements[0])
    for i in range(1, len(elements)-1):
        tree.add(elements[i], 1)
    return tree

def main():
    list_ = list(map(int, input().split()))
    tree = build_tree(list_)
    print(is_balanced(tree))
main()