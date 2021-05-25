class treeNode:
    __size = 0
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        treeNode.__size += 1

    def add(self, value):
        if value == self.data:
            return
        if value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = treeNode(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = treeNode(value)

    def findForks(self):
        if self.left:
            self.left.findForks()
        if (self.left and self.right is None) or (self.left is None and self.right):
            print(self.data)
        if self.right:
            self.right.findForks()

def buildTree(elements):
    result = treeNode(elements[0])
    for i in range(1, len(elements)):
        result.add(elements[i])
    return result

def main():
    numbers = list(map(int, input().split(" "))) 
    numbers.pop()
    tree = buildTree(numbers)
    tree.findForks()
 
main()