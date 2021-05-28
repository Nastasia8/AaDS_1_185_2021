#1
#class Node:#создаем класс связанный список
#    __size = 0 #указываем целочисленный тип данных
#    def __init__(self, data): #обьявление создания субьекта, то есть задаем метод init
#        self.data = data #дальше создаются атрибуты для метода init
#        self.left = None
#        self.right = None
#        Node.__size+=1 #задаем размер для дерева(вроде как)
#        
#    def add(self, value):#реализуем класс через функцию def add
#        if value == self.data:#создаем цикл с возвращением значения
#            return
#        if value < self.data:#еще цикл
#            if self.left:
#                self.left.add(value)
#            else:
#                self.left = Node(value)
#        else:
#            if self.right:
#                self.right.add(value)
#            else:
#                self.right = Node(value)
#                
#    def find_forks(self): #функци для нахождения ответвления и заданий в них значений в порядке возрастания
#        if self.left:
#            self.left.find_forks()
#        if self.left or self.right:
#            if self.left and not self.right:
#                print(self.data, end =" ")
#            elif not self.left and self.right:
#                print(self.data, end =" ")
#        if self.right:
#            self.right.find_forks()
#    def find_fork(self):
#        if self.left:
#            self.left.find_fork()
#        if (self.left and self.right is None) or (self.left is None and self.right):
#            print(self.data)
#        if self.right:
#            self.right.find_fork()
#def build_tree(elements): #создаем функцию для построения элементов, значения которых находили выше
#    r = Node(elements[0])
#    for item in range(1, len(elements)):
#        r.add(elements[item])
#    return r
#
#def main(): #создаем основную функцию для ввода списка в консоль с пробелом
#    n =list(map(int, input().split(" "))) 
#    n.pop()
#
#    tree = build_tree(n)
#
#    tree.find_fork()
# 
#main()
#2
#class Node:#создаем класс связанный список
#    def __init__(self, data):#обьявление создания субьекта, то есть задаем метод init
#        self.data = data#дальше создаются атрибуты для метода init
#        self.left = None
#        self.right = None
#        
#    def add(self, value):#реализуем класс через функцию def add
#        if value == self.data:
#            return
#        if value < self.data:
#            if self.left:
#                self.left.add(value)
#            else:
#                self.left = Node(value)
#        else:
#            if self.right:
#                self.right.add(value)
#            else:
#                self.right = Node(value)
#                
#def height(tree):#создаем функцию в которой возвращаем значения правой и левой веток
#    if tree is None:
#        return 0
#    return max(height(tree.left), height(tree.right)) + 1
#
#def build_tree(elements):#создаем функцию для построения дерева
#    root = Node(elements[0])
#    for item in range(1, len(elements)):# цикл для длины дерева с возвращением переменной root равной первому элементу
#        root.add(elements[item])
#    return root
#
#def check_balance(tree):#здесь я понял что мы делали это в классе и комментарии не нужны
#    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and check_balance(tree.right) and check_balance(tree.left)):
#        return True
#    return False
#    
#def main():
#    n =list(map(int, input().split(" "))) 
#    n.pop()
#
#    tree = build_tree(n)
#
#    if check_balance(tree):
#        print("YES")
#    else:
#        print("NO")
# 
#main()
#3
#from math import gcd
#def build(v,l,r,do,a):
#    if r - l == 1:
#        do[v]= a[l]
#        return
#    m=(r+l)//2
#    build(2*v+1,l,m,do,a)
#    build(2*v+2,m,r,do,a)
#    do[v] = gcd(do[2*v+1],do[2*v+2])
#
#def nod(v,l,r,do,ql,qr):
#    if ql<=l and qr>=r:
#        return do[v]
#    if ql >= r or qr<=l:
#        return 0
#    m = (r+l)//2
#    tl = nod (2*v+1,l,m,do,ql,qr)
#    tr = nod (2*v+2,m,r,do,ql,qr)
#
#    return gcd(tl,tr)
#
#def main():
#    n=int(input())
#    a= list(map(int, input().split(maxsplit=n)))
#    do= [0]*4*n
#    build(0,0,n,do,a)
#    q = int(input())
#    index = []
#    while q !=0:
#        l,r = map(int,input().split())
#        index.append(nod(0,0,n,do,l-1,r))
#        q-=1
#    print(*index)
#
#
#main()
#5
#from math import gcd
#def build(v,l,r,do,a):
#    if r - l == 1:
#        do[v]= a[l]
#        return
#    m=(r+l)//2
#    build(2*v+1,l,m,do,a)
#    build(2*v+2,m,r,do,a)
#    do[v] = gcd(do[2*v+1],do[2*v+2])
#
#def update(v,l,r,do,idx,value):
#    if r-l==1:
#        do[v]=value
#        return
#    m=(r+l)//2
#    if idx < m:
#        update (2*v+1,l,m,do,idx,value)
#    else:
#        update (2*v+2,m,r,do,idx,value)
#    do[v]= gcd (do[2*v+1],do[2*v+2])
#def nod(v,l,r,do,ql,qr):
#    if ql<=l and qr>=r:
#        return do[v]
#    if ql >= r or qr<=l:
#        return 0
#    m = (r+l)//2
#    tl = nod (2*v+1,l,m,do,ql,qr)
#    tr = nod (2*v+2,m,r,do,ql,qr)
#    return gcd(tl,tr)
#
#def main():
#    n=int(input())
#    a= list(map(int, input().split(maxsplit=n)))
#    do= [0]*4*n
#    build(0,0,n,do,a)
#    q = int(input())
#    index = []
#    while q !=0:
#        que,l,r = map(str,input().split())
#        if que=="s":
#            index.append(nod(0,0,n,do,int(l)-1,int(r)))
#        else:
#            update(0,0,n,do,int(l)-1,int(r))
#        q-=1
#    print(*index)
#
#
#main()
