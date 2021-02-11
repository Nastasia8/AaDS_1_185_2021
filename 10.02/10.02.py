#1

def factorial (x):
    s=1
    for i in range (1,x+1):
        s*=i
    if x==0:
        return 0
    else:
        return s

print (factorial(3))

#2

def f(n):
    if n==0:
        return 0
    if n==1:
        return 3
    if n==2:
        return 5
   
    return f(n-1)+f(n-2)+f(n-3)

n = 15
for i in range (n+1):
    print (f(i))

#3

h=int(input("h="))

for i in range(h):
    for j in range(h):
        if j<=i:
            print ("@",end ="")
    print()

print ()
for i in range(h):
    for j in range(h):
        if j>=i:
            print ("@",end ="")
    print()

print ()
i=1
while i< h+1:
    print(" "*(h+1-i),"@"*i)
    i+=1

print ()

i=0
while i< h+1:
    j=0
    while j < h+1:
        if (j>=i) and (j<h) and (i<h):
            print ("@",end ="")
        else:
            print (" ",end ="")
        j+=1
    print()
    i+=1



#4
def nod (x,y):
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x
    return x

x=int(input("x="))
y=int(input("y="))

print ("НОД x,y=",nod(x ,y))

#5 

x=int(input("x="))
y=int(input("y="))

def nok (x,y):
    return x*y/nod(x,y)

print ("НОК x,y=",round(nok (x,y)))

#6 

#a 
from math import gcd

def nod_mn (chisla):
    value=gcd(chisla[0],chisla[1])
    for i in range (2,len(chisla)):
        value=gcd(value,chisla[i])
    return value

print (nod_mn ([1000,1000,500,100,10]))

#b
def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans
def intersection (a,b):
    c=[]
    for i in a:
        if i in c: 
            continue
        for j in b:
            if i==j:
                c.append(i)
                break
    return c
                
def nod_mn_fact (chisla):
    list_result=Factor(chisla[0])
    
    for i in range (1,len(chisla)):
        list_result=intersection(list_result,Factor(chisla[i]))
    
    final_result=1
    for i in list_result:
        final_result*=i
    print ("Нод чисел =",final_result)

nod_mn_fact  ([78, 294, 570, 36,6])


