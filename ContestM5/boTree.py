

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
        
    def search(self, value):
        if self.data == value:
            return True

        if value < self.data:
            if self.left:
                return self.left.search(value)
            else: return False

        else:
            if self.right:
                return self.right.search(value)
            else: return False

    def delete(self, value):
        pass

    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.data, end=" ")
        if self.right:
            self.right.in_order_print()

    def find_forks(self):
        if self.left:
            self.left.find_forks()
        if self.right and self.left:
            print(self.data, end=" ")
        if self.right:
            self.right.find_forks()


#Questionable
def height(tree):
    if not tree:
        return 0
    return (max(height(tree.left), height(tree.left))+1)

def in_order(tree):
    if tree:
        in_order(tree.left)
        print(tree.data, end=" ")
        in_order(tree.right)

def pre_order(tree):
    if tree:
        print(tree.data, end=" ")
        pre_order(tree.left)
        pre_order(tree.right)

def post_order(tree):
    if tree:
        post_order(tree.left)
        post_order(tree.right)
        print(tree.data, end=" ")

def build_tree(elements):
    tree = Node(elements[0])
    for i in range(1, len(elements)):
        tree.add(elements[i], 1)
    return tree

def main():
    list_ = [7, 3, 2, 1, 9, 5, 4, 6, 8]
    tree = build_tree(list_)
    tree.in_order_print()
    print(" ")
    print(tree.size)
    print(tree.search(5))
    print(tree.search(0))
    print(" ")
    pre_order(tree)
    print(" ")
    in_order(tree)
    print(" ")
    post_order(tree)
    print(" ")
    tree.find_forks()
main()