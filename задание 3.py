#1

n=int(input("ввод числа "))
def funkx(n):
  spisok=[]
  if n<=0:
    print("Ай так нельзя ")
  while n>1:
    if int(n)%2==0:
      n=n/2
    else:
      n=(n/3+1)/2
    spisok.append(round(n))
  print(spisok)
funkx(n)

#2 new
def faktorial(n):
  factorial = 1
  while n > 1:
    factorial *= n
    n -= 1
  return n
n=10
def funk2(n):
  for k in range(1,n):
    x=-1*k*((5-k)/(faktorial(k)))
  print(x)

funk2(n)


#2 past
def funk1(n):
  if n==0:
    return 0
  if n==1:
    return 3
  if n==2:
    return 5
  return funk1(n-1)+funk1(n-2)+funk1(n-3)

for i in range(0, 16):
  print(funk1(i), end =" ")
#

#3
s1=["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]
s2=["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
s3=["tiger",  "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]

def funk3(s1,simv):
  maxi=0
  snew=[]
  for i in s1:
    if len(i)>maxi:
      maxi=len(i)
  for i in s1:
    if len(i)<maxi:
      a=maxi-len(i)
      i=i+(simv*a)
      snew.append(i)
    else:
      snew.append(i)
  print(snew)
funk3(s1,"X")
funk3(s2,"_")
funk3(s3,"+")
#5
sp = list(map(int, input("ввод чисел ").split()))
print(sp)
def funk5(sp):
  a=[]
  for i in sp:
    if i not in a:
      a.append(i)
  a.sort()
  return tuple(a)
x=funk5(sp)
print(x)
#6
def current_row(n):
    row=list()
    for i in range(n):
        if i==0 or i==n-1:
            row.append(1)
        else:
            c_row=current_row(n-1)
            row.append(c_row[i-1]+c_row[i])
    return row
def triangle(m):
    result=list()
    for i in range(m):
        result.append(current_row(i+1))
    ### beautify
    for j in result:
        print(j)
triangle(6)
#7
n = 30
def funk7(n):
  lst = []
  for i in range(2, n+1):
    for j in range(2, i):
      if i % j == 0:
        break
    else:
      lst.append(i)
  print(lst)
funk7(n)
#4

x=[5, 6, 9, 6, 3, 5, 2, 5, 1]
print(x)
def funk4(x):
  c=[]
  for i in range(len(x)):
    if x[i] not in c:
      c.append(x[i])
    else:
      s=0
      n=x[i]
      z=1
      while s<i:
        if x[s]==n:
          z+=1
        s+=1
      c.append(int(str(n)*z))
  print(c)
funk4(x)
