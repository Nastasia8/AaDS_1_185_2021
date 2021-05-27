#1
n = int(input("Vvedite chislo dlya vicheslenia fact = "))

fact = 1
while n > 1:
    fact *= n
    n -= 1
print(fact)

#2
def F(n):
    if n == 0:
        return 0
    if n == 1:
        return 3
    if n == 2:
        return 5
    if n > 2:
        return F(n-1) + F(n-2) + F(n-3)
        
n = 15
for i in range(n+1):
    print(F(i))

#4
x = int(input("Vvedite pervoe natur chislo = "))
y = int(input("Vvedite vtoroe natur chislo = "))
while x!=0 and y!=0:
    if x>y:
        x=x%y
    else:
        y=y%x
print("NOD (",x,";",y,")","=",x+y)

#5
x = int(input("Vvedite pervoe natur chislo = "))
y = int(input("Vvedite vtoroe natur chislo = "))
nod = 0
s = x*y
while x!=0 and y!=0:
    if x>y:
        x=x%y
    else:
        y=y%x
nod = x+y
print(s//(nod))