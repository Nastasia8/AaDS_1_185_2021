class Node: #объявление класса
    def __init__(self, data): #конструктор
        self.left = None
        self.right = None
        self.data = data
    def add(self, data): #Функция добавления элемента в дерево
        if data == self.data:
            return
        if data < self.data: #отрисовка по минимуму
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)

def height(tree): #высота дерева
    if not tree:
        return 0
    return max(height(tree.left), height(tree.right))+1 #максимальная высота правой или левой ветки; +1 - нумерация с 0

def is_balanced(tree):
    #Перебор всех условий равенства. Высота левой = Высоте правой или Высота левой +1 = высоте правой или Высота правой +1 = левой. и рекурсивая проверка равенства левой и правой ветки
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and is_balanced(tree.left) and is_balanced(tree.right)):
        return True
    return False

def build_tree(elements): #функция отрисовки дерева
    tree = Node(elements[0])
    for i in range(1, len(elements)-1):
        tree.add(elements[i])
    return tree

def main():
    list_ = list(map(int, input().split())) #считывание чисел
    tree = build_tree(list_)
    if is_balanced(tree): #функция вернет либо правду либо ложь, соответсвенно ответ будет да или нет
        print("YES")
    else:
        print("NO")
main()