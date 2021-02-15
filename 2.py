# #1
# n = int(input())
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(n))

# #2
# def fun(n):
#     if n > 2:
#         return fun(n-1) + fun(n-2) + fun(n-3)
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 3 
#     elif n == 2:
#         return 5
# print(fun(n))

# #3
# h = int(input())
# symbol = input()
# c = 1
# def drawing1(h, symbol):
#     for i in range(1, h+1):
#         print(symbol*i)
#     print('\n')
#     for i in range(1, h+1):
#         print(symbol*((h+1)-i))
#     print('\n')
# def drawing2(h, symbol, c):
#     while h >= c:
#         print(' ' * (h - c), symbol*c)
#         c+=1
#     print('\n')
# def drawing3(h, symbol, c):
#     while h >= c:
#         print(' ' * (c-1), symbol*((h+1)-c))
#         c+=1
# drawing1(h, symbol)
# drawing2(h, symbol, c)
# drawing3(h, symbol, c)

#4
# def nod(a, b):
#     while a != b:
#         if a > b:
#             a = a - b
#         else:
#             b = b - a
#     print(a)
# nod(18, 48)
# nod(48, 16)

#5
# def nod(a, b):
#     if a < b:
#         a, b = b, a
#     while b:
#         a %= b
#         a, b = b, a
#     return a
#
# def nok(a, b):
#     return a / nod(a, b) * b
#
# print(nok(24, 44))


#6
def nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a %= b
        a, b = b, a
    return a
n = int(input())
arr = []
a = 0
for i in range(1, n):
    arr.append(int(input('> ')))
arr = sorted(arr)
for i in range(1, len(arr)):
    a = nod(arr[i-1], arr[i])
print(a)

