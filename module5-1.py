class No:
    __size = 0
    __height = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        No.__size += 1

    @property
    def size(self):
        return self.__size

    @property
    def height(self):
        return self.__height + 1

    def add(self, value, depth):
        if self.data == value:
            return
        if value < self.data:
            if self.left:
                self.left.add(value, depth + 1)
            else:
                if No.__height < depth:
                    No.__height = depth
                self.left = No(value)
        else:
            if self.right:
                self.right.add(value, depth + 1)
            else:
                if No.__height < depth:
                    No.__height = depth
                self.right = No(value)

    def find_forks(self):
        if self.left:
            self.left.find_forks()
        if self.left and not self.right:
            print(self.data)
        if self.right and not self.left:
            print(self.data)
        if self.right:
            self.right.find_forks()

def build_tree(elements):
    tree = No(elements[0])
    for i in range(1, len(elements)):
        tree.add(elements[i], 1)
    return tree

def main():
    elements = list(map(int, input().split()))
    tree = build_tree(elements[:len(elements)-1])
    tree.find_forks()

main()