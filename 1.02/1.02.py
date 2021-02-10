

#5
def stepenspepen (y,z):
    numbers= [i**y**z if i%2==1  else i   for i in range (1,21)]
    return numbers

print (stepenspepen (2,3))

#6
list_a= "Hello hi how hello are and you I am fine thank you and you hello You Thank And".lower().split(" ")
b={i:list_a.count(i) for i in list_a}
print (b)

#7 --------------------------------------------------------------------------------
import random
n=int(input("Введите n:"))
arr2=[[random.randint(1,20) for j in range(n)] for i in range(n)]

def proizv ():
    print (arr2)
    z=n
    for i in range (0,n):
        z-=1
        arr2[i][z]=arr2[i][z]*2

    for i in range (n):
        for j in range (n):
            print(arr2[i][j], end='\t')
        print()

    
proizv()

#8 --------------------------------------------------------------------------------
from random import randrange
m,n = int(input("Столбец:")),int(input("Строка:"))
array = [[randrange(0,11) for _ in range(m)] for _ in range(n)]

#1 способ 1
def print_Arr ():
    print ("-----------------------")
    for i in range(n):
        for j in range(m):
            print(array[i][j],end = '\t')
        print()

print_Arr()
for i in range(n):
    c = m-1
    for j in range(m//2):
        t = array[i][j]
        array[i][j] = array[i][j+c]
        array[i][j+c] = t
        c -= 2
print_Arr()

# способ 2
for i in array:
    i.reverse()
print_Arr()

#3 способ 3
array=[i[::-1] for i in array]
print_Arr()   

# 9
print()
def function (a,b):
    check=len(a)
    a.update(b)
    if len(a)==check:
        return True
    else:
        return False

print (function ({1,4,6,7,3,8,5},[1,2,4]))

print (function ({1,4,6,7,3,8,5},[1,4,7]))

# 10 -------------------------------------------------------

list_10 = [6, 43, -2, 11, -55, -12, 3, 345, 0]




print ()

# 11 ------------------------------------------------------
print()

class Human:
    def __init__(self,name,secondname,hometown,birth_date):
        self.__name=name
        self.__secondname=secondname
        self.__hometown=hometown
        self.__birth_date=birth_date

    def Show (self):
        print ("Name:", self.__name, "\nSecondname:" , self.__secondname, "\nHometown:",self.__hometown,"\nBirth: ",self.__birth_date)
    def Get_Age (self,current_year):
        return current_year-self.__birth_date
         
class Student(Human):
    def __init__(self,name,secondname,hometown,birth_date,university):
        Human.__init__(self,name,secondname,hometown,birth_date)
        self.__university=university
    def Show_Study (self):
        print ("Studying in",self.__university)

class Teacher(Human):
    
    def __init__(self, name, secondname, hometown, birth_date,work):
        super().__init__(name, secondname, hometown, birth_date)
        self.__work=work
    
    def Show_Work (self):
        print ("Working in",self.__work)
        



first = Student ("Dasha","Ovchinnikova","Ivanovo",2002,"ISU")
first.Show()
first.Show_Study()

second = Teacher ("Tatyana","Korhova","Moscow",1970,"Second school of Ivanovo")
second.Show()
second.Show_Work()





