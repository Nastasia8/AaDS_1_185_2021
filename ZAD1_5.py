class Node:
    __size = 0
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.__size+=1
        
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
                
    def find_forks(self):
        if self.left:
            self.left.find_forks()
        if self.left or self.right:
            if self.left and not self.right:
                print(self.data, end =" ")
            elif not self.left and self.right:
                print(self.data, end =" ")
        if self.right:
            self.right.find_forks()
    def find_fork(self):
        if self.left:
            self.left.find_fork()
        if (self.left and self.right is None) or (self.left is None and self.right):
            print(self.data)
        if self.right:
            self.right.find_fork()
def build_tree(elements):
    r = Node(elements[0])
    for item in range(1, len(elements)):
        r.add(elements[item])
    return r

def main():
    n =list(map(int, input().split(" "))) 
    n.pop()

    tree = build_tree(n)

    tree.find_fork()
 
main()