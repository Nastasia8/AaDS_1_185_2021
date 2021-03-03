#1

import math
n = int(input("Введите число: "))
print (math.factorial(n))

#2

def function(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    elif n == 2:
        return 5
    elif n > 2:
        return(function(n-1) + function(n-2) + function(n-3))
for n in range(16):
    print(function(n))  

#3

x = int(input("Введите высоту треугольника:"))
y = 0
while x > y:
    print (y * "◘")
    y += 1
while y >= 1:
    print (y * "◘")
    y -= 1
if x == 0:
    print ("Так не бывает на свете, чтоб была высота у треугольника ноль")

#4

import math
x = int(input("Первое число: "))
y = int(input("Второе число: "))
def _gcd(x, y):
    return(gcd(x, y))

print(_gcd(x, y))

#5

import math
x = int(input("Первое число: "))
y = int(input("Второе число: "))
def _lcm(x, y):
    return(lcm(x, y))

print(_lcm(x, y))
