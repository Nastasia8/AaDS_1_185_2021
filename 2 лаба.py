##1 
def funk(n):
  factorial=1
  for i in range(2, n+1):
    factorial *= i
  print(factorial)
funk(0)
##4
x=int(input("x = "))
y=int(input("y = "))
def NOD(m,n):
  j=x
  j1=y
  while m> 0 and n> 0:
    if m>n:
      m=m%n
    else:
      n=n%m
  print("НОД ("+str(j)+";"+ str(j1)+") = "+str(m+n))
NOD(x,y)
##5
def NOK(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)
a=18
b=48
c=NOK(a,b)
print("НОК ("+str(a)+";"+str(b)+") = "+str(c))