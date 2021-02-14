#1
def funk1(n):
  factorial=1
  for i in range(2, n+1):
    factorial *= i
  print(factorial)
funk1(5)
#2
#f(0)=0, f(1)=3, f(2)=5.
#3
s=5
def funk3(s):
  for i in range(s):
    for j in range(s):
      if i+j<s:
        print("0 ",end="")
    print("")
  print(" ")
  for i in range(s):
    for j in range(s):
      if i>=j:
        print("0 ",end="")
    print("")
  print("")
  i=0
  j=0
  while i<=s:
    while j<=s:
      #print(i,j)
      if i+j>s:
        print("0 ",end="")
      else:
        print("  ",end="")
      j+=1
    j=0
    i+=1
    print("")
  print("")
  i=0
  j=0
  while i<=s:
    while j<=s:
      #print(i,j)
      if j>i:
        print("0 ",end="")
      else:
        print("  ",end="")
      j+=1
    j=0
    i+=1
    print("")
  print("")
funk3(s)
#4
x=int(input("x = "))
y=int(input("x = "))
def funk4(a,b):
  h=x
  h1=y
  while a> 0 and b> 0:
    if a>b:
      a=a%b
    else:
      b=b%a
  print("НОД ("+str(h)+";"+ str(h1)+") = "+str(a+b))
funk4(x,y)

#5
def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)
a=23
b=16
d=nok(a,b)
print("НОК ("+str(a)+";"+str(b)+") = "+str(d))
#6
spisok=[26,32,64,10,20,28]
def funkx(a,b):
  while a> 0 and b> 0:
    if a>b:
      a=a%b
    else:
      b=b%a
  return (a+b)
def funk6(spisok):
  i=0
  mini=100000
  a=int(spisok[0])
  while i <(len(spisok)-1):
    b=int(spisok[i+1])
    x=funkx(a,b)
    if x<mini:
      mini=x
    a=mini
    i+=1
  print("nod = "+str(mini))
funk6(spisok)
#6.2