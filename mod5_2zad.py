#7 3 2 1 9 5 4 6 8 0
#YES
class Node:
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
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)
                
def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right)) + 1

def build_tree(elements):
    root = Node(elements[0])
    for item in range(1, len(elements)):
        root.add(elements[item])
    return root

def check_balance(tree):
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and check_balance(tree.right) and check_balance(tree.left)):
        return True
    return False
    
def main():
    n =list(map(int, input().split(" "))) 
    n.pop()

    tree = build_tree(n)

    if check_balance(tree):
        print("YES")
    else:
        print("NO")
 
main()