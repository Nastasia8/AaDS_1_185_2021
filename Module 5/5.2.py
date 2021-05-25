class treeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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

def heightCheck(tree):
    if not tree:
        return 0
    else:
        return max(heightCheck(tree.left), heightCheck(tree.right)) + 1

def treeIsBalanced(tree):
    if not tree or ((heightCheck(tree.left) - heightCheck(tree.right) == -1 or heightCheck(tree.left) - heightCheck(tree.right) ==  0 or heightCheck(tree.left) - heightCheck(tree.right) == 1) and treeIsBalanced(tree.left) and treeIsBalanced(tree.right)):
        return True
    else:
        return False

def buildTree(elements):
    result = treeNode(elements[0])
    for i in range(1, len(elements) - 1):
        result.add(elements[i])
    return result

def main():
    numbers = list(map(int, input().split(" "))) 
    tree = buildTree(numbers)
    if treeIsBalanced(tree):
        print("YES")
    else:
        print("NO")
 
main()