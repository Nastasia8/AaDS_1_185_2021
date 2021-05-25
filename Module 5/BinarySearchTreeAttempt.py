class Node:
    def __init__(self, value = None):
        self.value = value
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, currentNode):
        if value < currentNode.value:
            if currentNode.leftChild == None:
                currentNode.leftChild = Node(value)
            else:
                self._insert(value, currentNode.leftChild)
        elif value > currentNode.value:
            if currentNode.rightChild == None:
                currentNode.rightChild = Node(value)
            else:
                self._insert(value, currentNode.rightChild)

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)

    def _printTree(self, currentNode):
        self._printTree(currentNode.leftChild)
        print(str(currentNode.value))
        self._printTree(currentNode.rightChild)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, currentNode, currentHeight):
        if currentNode == None:
            return currentHeight
        leftHeight = self._height(currentNode.leftChild, currentHeight + 1)
        rightHeight = self._height(currentNode.rightChild, currentHeight + 1)
        return max(leftHeight, rightHeight)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False
    
    def _search(self, value, currentNode):
        if value == currentNode.value:
            return True
        elif value < currentNode.value and currentNode.leftChild != None:
            return self._search(value, currentNode.leftChild)
        elif value > currentNode.value and currentNode.rightChild != None:
            return self._search(value, currentNode.rightChild)
        return False
'''
def fillTree(tree, n, maxInt = 1000):
    from random import randint
    for _ in range(n):
        currentElement = randint(0, maxInt)
        tree.insert(currentElement)

def main():
    tree = BinarySearchTree()
    n = int(input)
    tree = fillTree(tree, n)
    tree.printTree()
'''
tree = BinarySearchTree()

tree.insert(32)
tree.insert(-1)
tree.insert(46)
tree.insert(45)
tree.insert(6)

tree.printTree()

print(str(tree.height()))

print(tree.search(-1))
print(tree.search(1))