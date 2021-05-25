class Node:#класс дерево
    def __init__(self, data):#конструктор базовый
        self.data = data
        self.left = None
        self.right = None

    def add(self, value):#функция добавления элемента в дерево
        if self.data == value:
            return
        if value < self.data:#строим дерево по минимуму
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

    def check_tree(self):#функция проверки деревьев на наличие разной длины
        if self.left and self.right:
            if abs(height(self.right) - height(self.left)) > 1:#еслисуществует правая и левая ветка и разница между их высотами больше 1, вовращаем нет
                return "NO"
        else:
            if not self.right and self.left and height(self.left) > 1:#если есть только левая и её высота больше 1
                return "NO" 
            if not self.left and self.right and height(self.right) > 1:#если есть только правая и её высота больше 1
                return "NO"
        if self.left:
            if self.left.check_tree() == "NO":#рекурсивно проходим по левой ветке, если уже было НЕТ, то возвращаем НЕТ
                return "NO"
        if self.right:    
            if self.right.check_tree() == "NO":#рекурсивно проходим по правой ветке
                return "NO"

def built_tree(elements):#функция постройки дерева
    tree = Node(elements[0])
    for i in range(1, len(elements)):
        tree.add(elements[i]) #каждое число по очереди добаляем в дерево
    return tree

def height(tree):#функция поиска высоты дерева
    if not tree:
        return 0
    return (max(height(tree.left), height(tree.right))+1) #выводит максимум из рекурсивного вызыва правой и левой части +1, так как нумерация с 0

num = list(map(int, input().split()))#ввод чисел в список
num.pop()
num = built_tree(num)#вызов функции постройки дерева
print(num.check_tree()) if num.check_tree() == 'NO' else print("YES")#вывод результата поиска деревьев, если это НЕТ, иначе вывод ДА
