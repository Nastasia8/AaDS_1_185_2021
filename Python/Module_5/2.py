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
        if self.left and not self.right:
            if not self.left.left and self.left.right:
                return
            else:
                if self.left.left.left or self.left.left.right:
                    print('NO')
                    return
        if self.right and not self.left:
            if self.right.right.left or self.right.right.right:
                print('NO')
                return
        print("YES")
        return                            

            


def built_tree_and_check(num):
    tree = Node(num[0])
    for i in range(1, len(num)):
        tree.add(num[i])
    tree.display()    
    return tree    


num = list(map(int, input().split()))
num.pop()
built_tree_and_check(num)