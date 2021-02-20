# #2
# arr0 = [i for i in range(1,21,2)]
# p=[]
# for j in arr0:
#     p.append(j**2)
# arr = [*range(1,21,2)]
# arr2 = [i**2 for i in arr]
# print(arr2)

# #3
# def function(k):
#     for n in range(1, k+1):
#         result = 2**n-1
#         print(result)
# k = int(input('K: '))
# function(k)

# #4 
# arr3 = [7,1,3,4,3,9,14,-5,-17,-13,-19,-18]
# sum = 0
# for i in arr3[::-1]:
#     if i<0: 
#         sum+=i
#     else:
#         break
# print(sum)
# f=0
# sum2=0
# while f < len(arr3):
#     if arr3[f]<0:
#         sum2+=arr3[f]
#     f+=1
# print(sum2)

# #5
# y = int(input('y: '))
# z = int(input('z: '))
# some = [x**y**z for x in range(1,21)]
# print(some)

# #6
# string = 'Hello hi how hello are and you I am fine thank you and you hello You Thank And'
# a = string.split()
# di = {}
# for i in a:
#     di[i] = 0
#     for j in a:
#         if i.lower() == j.lower():
#             di[i] += 1
# print(di)

#7
# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# def show(matrix):
#     for i in range(len(matrix)):
#         for j in matrix[i]:
#             print(j, end='  ')
#         print('\n')
# def func(matrix):
#     for i in range(len(matrix)):
#         matrix[i][2-i] *= 2
# show(matrix)
# print('--------------------')
# func(matrix)
# show(matrix)

#8
# from random import randint
# n = int(input("n = "))
# m = int(input('m = '))
# arr = [[0]*m]*n
# arr = [[arr[i][j] + randint(1, 10) for j in range(m)]for i in range(n)]
# print(arr, '\n')
# for i in range(n):
#     for j in range(m//2):
#         arr[i][j], arr[i][-(j+1)] = arr[i][-(j+1)], arr[i][j]
# for i in range(n):
#     arr[i] = arr[i][::-1]
# print(arr)


#9
# def checking(p, a):
#     if p.issubset(a) and len(p) == len(a):
#         return True
#     else:
#         return False
# checking({*range(1,10)}, [*range(1,10, 2)])

#10
# arr = [6, 43, -2, 11, -55, -12, 3, 345, 0]
# print({x:'positive' if x > 0 else 'negative' if x < 0 else 'zero' for x in arr})


#11
# class Person:
#     def __init__(self, name, lastname, pb, year, age):
#         self.name = name
#         self.lastname = lastname
#         self.pb = pb
#         self.year = year
#         self.age = age
#
#     @property
#     def Age(self):
#         return self.age
#
#     def Show(self):
#         print(f'Name: {self.name}, Lastname: {self.lastname}, Place of birth: {self.pb}, Year: {self.year}, Age: {self.age}')
#
# class Student(Person):
#     def __init__(self, answer, name, lastname, pb, year, age):
#         self.answer = answer
#         super().__init__(name, lastname, pb, year, age)
#     def attendance(self):
#         super().Show()
#         if self.answer == 'yes':
#             print('The student was at University today')
#         else:
#             print('The student was not at University today')
#
# class Teacher(Person):
#     def __init__(self, object_, name, lastname, pb, year, age):
#         self.object_ = object_
#         super().__init__(name, lastname, pb, year, age)
#     def object(self):
#         super().Show()
#         print(f'Professor teaches {self.object_}')
#
# person = Person('Jonny', 'Montano', 'New Yerk', 1999, 22)
# student = Student('yes', 'Jack', 'Moly', 'LA', 2001, 20)
# student.attendance()
# professor = Teacher('Math', 'Nick', 'Armstrong', 'Alabama', 1975, 46)
# professor.object()
