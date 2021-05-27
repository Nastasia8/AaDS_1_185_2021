class Node:                    #создаем класс связанный список
    def __init__(self, data):                   #обьявление создания субьекта, то есть задаем метод init
        self.data = data                             #дальше создаются атрибуты для метода init
        self.left = None
        self.right = None
        
    def add(self, value):                                 #реализуем класс через функцию def add
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
                
def height(tree):                         #создаем функцию в которой возвращаем значения правой и левой веток
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right)) + 1

def build_tree(elements):                              #создаем функцию для построения дерева
    root = Node(elements[0])
    for item in range(1, len(elements)):                       # цикл для длины дерева с возвращением переменной root равной первому элементу
        root.add(elements[item])
    return root

def check_balance(tree):                          #это мы делали в на паре 
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