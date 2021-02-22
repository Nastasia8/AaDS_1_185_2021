##2
list1=list(range(1,20,2))
list2=[]
print(list1)
for i in list1:
  list2.append(i**2)
print(list2)
##3
k=int(input("k = "))
def funkciya(k):
  for i in range(1,k):
    x=(2**i)-1
  print(x)
funkciya(k)
##4
s=[7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
r=0 
i=0 
while i<12:
    if s[i]<0:
        r=r+s[i]
    i=i+1
print(r)
##5 
'''
почему-то с данными переменными не работает
list2=list(range(1,20))
def funk(list2,y,z):
  new_list=[]
  for i in list2:
    if i%2!=0:
       new_list.append((i**y)**z)
  return  new_list
 new_list=funk(list2,3,2)
print(new_list)
'''
spisok=list(range(1,20))
def funk(spisok,y,z):
  spisoknew=[]
  for i in spisok:
    if i%2!=0:
      spisoknew.append((i**y)**z)
  return spisoknew
spisoknew2=funk(spisok,3,2)
print(spisoknew2)
##6
text="Hello hi how hello are and you I am fine thank you and you hello You Thank And"
text=text.lower()
text=text.split(" ")
dictionary=dict={}
for i in text:
  if i not in dictionary:
    dictionary[i]=1
  else:
    dictionary[i]=dictionary[i]+1
print(text)
print(dictionary)
##7 
s=4
from random import *
mas =[[0 for j in range(s)] for i in range(s)]
for i in range(s):
  for j in range(s):
    mas[i][j] = randint(0,9)
  print(mas[i])
print(" ")
def funk7(mas,s):
  mas2 =[[0 for j in range(s)] for i in range(s)]
  for i in range(s):
    for j in range(s):
      if i+j==s-1:
        mas2[i][j] = mas[i][j]*2
      else:
        mas2[i][j] = mas[i][j]
  return mas2
mas2=funk7(mas,s)
for i in range(s):
  print(mas2[i])
##9
def Function(a,b):
    for i in b:
        if i not in a:
            return False
    return True

print(Function({1,2,3},[5]))
print(Function({1,2,3},[1,2]))
print(Function({1,2,3},[1,2,5]))
##10
spisok_new=[6, 43, -2, 11, -55, -12, 3, 345, 0]
def funk2(spisok_new):
  dictionary2={}
  for i in spisok_new:
    if i>0:
      dictionary2[i]="positive"
    if i<0:
      dictionary2[i]="negative"
    if i==0:
      dictionary2[i]="zero"
  return dictionary2
dictionary2=funk2(spisok_new)
print(dictionary2)
