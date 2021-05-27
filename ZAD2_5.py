class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    # @property
    # def height(self):
    #     return self.__height + 1


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



    def check_tree(self):
        if self.left and self.right:
            # print(abs(height(self.right) - height(self.left)))
            if abs(height(self.right) - height(self.left)) > 1:
                return "NO"
        else:
            if not self.right and self.left and height(self.left) > 1:
                return "NO" 
            if not self.left and self.right and height(self.right) > 1:
                return "NO"
        if self.left:
            if self.left.check_tree() == "NO":
                return "NO"
        if self.right:    
            if self.right.check_tree() == "NO":
                return "NO"


def built_tree(elements):
    tree = Node(elements[0])
    for i in range(1, len(elements)):
        tree.add(elements[i]) 
    return tree

def height(tree):
    if not tree:
        return 0
    return (max(height(tree.left), height(tree.right))+1)   


def main():
    num = list(map(int, input().split()))
    num.pop()
    num = built_tree(num)
    print(num.check_tree()) if num.check_tree() == 'NO' else print("YES")
main()