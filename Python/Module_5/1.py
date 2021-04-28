class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, value):
        if self.data == value:
            return
        if value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

    def display(self):
        if self.left:
            self.left.display()
        # print(self.data, end=" ")
        if not self.right and self.left:
            print(self.data, end=" ")
        elif not self.left and self.right:
            print(self.data, end=" ")    
        if self.right:
            self.right.display()


def built_tree(num):
    tree = Node(num[0])
    for i in range(1, len(num)):
        tree.add(num[i])
    return tree


num = list(map(int, input().split()))
num.pop()
built_tree(num).display()
