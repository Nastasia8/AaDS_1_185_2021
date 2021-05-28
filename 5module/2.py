class Node:

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
    
def build_tree(elements):
    tree = Node(elements[0])
    for i in range(1, len(elements)-1):
        tree.add(elements[i])
    return tree

def check(tree):
    if not tree:
        return True
    if  abs(height(tree.left)-height(tree.right))<=1 and check(tree.left) and check(tree.right):
        return True 
    return False



def main():
    elements = list(map(int, input().split()))

    tree = build_tree(elements)
    if check(tree):
        print("Yes")
    else:
        print("No")

main()