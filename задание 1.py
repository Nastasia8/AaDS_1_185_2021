##2
spisok=list(range(1,20,2))
spisok2=[]
print(spisok)
for i in spisok:
  spisok2.append(i**2)
print(spisok2)
##3
k=int(input("k = "))
def funkk(k):
  for i in range(1,k):
    x=(2**i)-1
  print(x)
funkk(k)
##4
spisoknew=[7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
x=0
for i in spisoknew:
  if i<0:
    x+=i
print("x = " +str(x))
x=0
i=0
while i < len(spisoknew):
  if spisoknew[i]<0:
    x+=spisoknew[i]
  i+=1
print("x2 = " +str(x))
##5
def funk5(spisok,y,z):
  spisoknew2=[]
  for i in spisok:
    if i%2!=0:
      spisoknew2.append((i**y)**z)
  return spisoknew2
spisoknew2=funk5(spisok,3,2)
print(spisoknew2)

##6
text="Hello hi how hello are and you I am fine thank you and you hello You Thank And"
text=text.lower()
text=text.split(" ")
dict1=dict={}
for i in text:
  if i not in dict1:
    dict1[i]=1
  else:
    dict1[i]=dict1[i]+1
print(text)
print(dict1)
##7
s=4
from random import *
massiv =[[0 for j in range(s)] for i in range(s)]
for i in range(s):
  for j in range(s):
    massiv[i][j] = randint(0,9)
  print(massiv[i])
print(" ")
def funk7(massiv,s):
  massiv2 =[[0 for j in range(s)] for i in range(s)]
  for i in range(s):
    for j in range(s):
      if i+j==s-1:
        massiv2[i][j] = massiv[i][j]*2
      else:
        massiv2[i][j] = massiv[i][j]
  return massiv2
massiv2=funk7(massiv,s)
for i in range(s):
  print(massiv2[i])
  
##8
mas1=[[4,3,5,1],[0,7,2,9],[2,6,3,8]]
for i in range(3):
  print(mas1[i])
print(" ")
mas2=[[13,97,56],[17,23,85],[22,45,66]]
for i in range(3):
  print(mas2[i])
print(" ")

def funk8(mas2):
  l=len(mas2)
  mas3 =[[0 for j in range(l)] for i in range(l)]
  for i in range(l):
    k=0
    j=2
    while j>=0:
      mas3[i][k]=mas2[i][j]
      k+=1
      j-=1
  for i in range(3):
    print(mas3[i])
funk8(mas2)
print(" ")
def funk81(mas1):
  l=len(mas1)
  mas3 =[[0 for j in range(4)] for i in range(l)]
  for i in range(l):
    k=0
    for j in range(3,-1,-1):
      mas3[i][k]=mas1[i][j]
      k+=1
  for i in range(l):
    print(mas3[i])
funk81(mas1)

##9
num_set = {1, 2, 3, 4, 5, 6} 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
def funk9(num_set,numbers):
  for i in num_set:
    if i not in numbers:
      return False
  return True
r=funk9(num_set,numbers)
print(r)
##10
spisokn=[6, 43, -2, 11, -55, -12, 3, 345, 0]
def funk10(spisokn):
  dict2={}
  for i in spisokn:
    if i>0:
      dict2[i]="positive"
    if i<0:
      dict2[i]="negative"
    if i==0:
      dict2[i]="zero"
  return dict2
dict2=funk10(spisokn)
print(dict2)
##11
class Human:
  def __init__(self, name,surname,placeofbirth,data):
    self.name = name
    self.surname = surname
    self.placeofbirth = placeofbirth
    self.data = data
  def Show(self):
    print("name "+self.name+" surname "+self.surname+" placeofbirth "+self.placeofbirth+" data "+str(self.data))
  def GetAge(self):
    print(str(2021-self.data)+" age")
class Student(Human):
  def __init__(self, name,surname,placeofbirth,data,course):
    super().__init__(name,surname,placeofbirth,data)
    self.course = course
  def xalava(self):
    print("халява приди к курсу номер "+str(self.course))
class Ticher(Human):
  def __init__(self, name,surname,placeofbirth,data,subject):
    super().__init__(name,surname,placeofbirth,data)
    self.subject = subject
  def subjectshow(self):
    print("subject -> "+self.subject)
Petr=Human("Petr","Fedorov","Ivanovo",2003)
Petr.Show()
Petr.GetAge()
print(" ")
Kiril=Student("Kiril","Ivanov","kineshma",2002,1)
Kiril.Show()
Kiril.xalava()
print(" ")
Sergei=Ticher("Sergei","Petrov","kineshma",1986,"math")
Sergei.Show()
Sergei.subjectshow()
