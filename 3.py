#1
# n = float(input('n: '))
# arr = []
# def fun(n):
#     while n > 1:
#         if n % 2 == 0:
#             n /= 2
#             arr.append(n)
#         else:
#             n = ((n * 3) + 1 )/ 2
#             arr.append(n)
#     return n
# print(fun(n))
# print(arr)
#2
# result = 1
# def fuc(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fuc(n-1)
# def somebody(n):
#     for i in range(1, n+1):
#         result = i * (-1) * ((5 - i)/fuc(i))
#     return result
# print(somebody(n))

#3
# def adding(a, symbol):
#     w = a[0]
#     for i in a:
#         if len(i) > len(w):
#             w = i
#     for i in range(0,len(a)):
#         if len(a[i])<len(w):
#             s = len(w) - len(a[i])
#             a[i] += symbol*s
#     return a
# symbol = '$'
# a = ['Bass', 'Roach', 'CatFish', 'Trout', 'Mackerel', 'Anchovy']
# b = ['Clematis', 'Dahlia', 'Rose', 'Chrysanthemum', 'Freesia', 'Lily', 'Peony']
# c = ['tiger', 'leopard', 'elephant', 'camel', 'fox', 'wolf', 'raccoon']
# print(adding(a, symbol))
# print(adding(b, symbol))
# print(adding(c, symbol))

#4
# def glass(f):
#     c = 1
#     rrr2 = []
#     rrr2.append(f[0])
#     for i in range(1, len(f)):
#         for j in rrr2:
#             if f[i]==j:
#                 c+=1
#                 rrr2.append(str(f[i])*c)
#                 c = 1
#             else:
#                 rrr2.append(f[i])
#     print(rrr2)
#
# rrr = [5, 6, 9, 6, 3, 5, 2, 5, 1]
# glass(rrr)

#5
# def f(something):
#     something = set(something)
#     return tuple(something)
# something = []
# n = int(input('N: '))
# for i in range(0, n):
#     something.append(int(input('> ')))
# print(f(something))

#6
# n = int(input('n: '))
# def factorial(l):
#     if l > 0:
#         return l*factorial(l-1)
#     return 1
# def triangle(n):
#     a = 1
#     b = 1
#     f = 1
#     for i in range(0, n):
#         arr = [0]*f
#         for j in range(0, f):
#             arr[j] = (factorial(i)/((factorial(j))*factorial(i-j)))*(a**j)*(b**(i-j))
#         print(arr)
#         f+=1
# triangle(n)

#7
from math import *
n = int(input('N: '))
rrr = [*range(1, n+1)]
def N(n, rrr):
    for i in range(1, len(rrr)):
        if i > round(sqrt(n)):
            rrr.sort()
            return rrr[rrr.count(0):len(rrr)]
        else:
            for j in range(1, len(rrr)):
                if rrr[i] != 0 and rrr[j]!=0 and rrr[j] % rrr[i] == 0 and rrr[i]!=rrr[j] :
                    rrr[j] = 0

print(N(n, rrr))