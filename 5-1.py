class Tree():#класс дерево, определяем поля высота и размер
    __size=0
    __height=0
    def __init__(self, data):#конструктор
        self.data=data
        self.left=None
        self.right=None
        Tree.__size+=1

    @property#свойство размера для доступа к нему
    def size(self):
        return self.__size
        #getter
    @property#свойство высоты 
    def height(self):
        return self.__height +1
    def find_forks(self):#поиск ветвей функция
        if self.left:
            self.left.find_forks()#если есть левый потомок, то рекурсивно вызываем
        if (self.right and not self.left) or (self.left and not self.right):
            print(self.data)#если есть только 1 потомок, то выводим данные
        if self.right:
            self.right.find_forks()#если есть правыйпотомок, то вызываем его
            
 
    def add(self, value,depth):#функция добавления элемента в дерево
        if self.data== value:
            return#если значение равно элементу, то ничего не возвращаем
        if value<self.data:#если значение меньше элемента
            if self.left:
                self.left.add(value,depth+1)#добавляем в левую ветку
            else:
                if Tree.__height< depth:
                    Tree.__height=depth#
                self.left= Tree(value)
        else:
            if self.right:
                self.right.add(value,depth+1)#добавляем в правуюветку
            else:
                if Tree.__height< depth:
                    Tree.__height=depth
                self.right= Tree(value)#

def bild_tree(elements):#создание дерева
    tree= Tree(elements[0])#постройка дерева по списку
    for i in range(1,len(elements)):
        tree.add(elements[i],1)#постепенное добавление элементов
    return tree
        
elements=list(map(int, input().split(" ")))#создание списка для вводаэлементов
elements=elements[:-1]#убираем последний элемент
tree= bild_tree(elements)
tree.find_forks()#поиск веток