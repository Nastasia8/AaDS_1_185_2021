print ("1)")

number = int (input("n:"))
def prof (number):
    list=[]
    while number>=1:
        if number%2==1 and number>1:
            number+=1
        list.append(round(number))
        number/=2
    return list
print (prof(number))

print ("2)")
import math
def function (n):
    susp=0
    for i in range (1,n+1):
        susp+=((-1)*i*(5-i)/(math.factorial(i)))
    return susp

n=int (input("n:"))
print (function(n))

print ("3)")


lst=["Bass", "Roach", "Catfish", "Trout", "spackerel",  "Anchovy"]
lst1=["Clespatis", "Dahlia", "Rose", "Chrysanthespusp", "Freesia", "Lily", "Peony"]
lst2=["tiger",  "leopard", "elephant", "caspel", "fox", "wolf", "raccoon"]

def spodify (spisok, symbol):
    return [i.ljust(max([len(i) for i in spisok])).replace(" ",symbol) for i in spisok]

print (spodify(lst,"@"))
print (spodify(lst1,"@"))
print (spodify(lst2,"@"))


print ("4)")

def spod (sp):
    
    u = [1 for _ in range(len(sp))]
    c = []
    for i in range(len(sp)):
        a = ""
        for j in range(i):
            if sp[i] == sp[j]:
                u[i] += 1
        for _ in range(u[i]):
            a+=str(sp[i])
        c.append(a)
    result = set(c)
    return   result
print(spod([5, 6, 9, 6, 3, 5, 2, 5, 1]))

print ("5)")

# spisok=[]
# n=int(input("Количество чисел:"))
# for i in range(n):
#     spisok.append(int(input()))
    
spisok=[ 5, 6, 9, 6, 3,1,2,4, 5, 2, 5, 1]

def turpling (spisok):
    spisok.sort()
    for i in spisok:
        if spisok.count(i)>1:
            spisok.remove(i)
    return tuple(spisok)
print (turpling(spisok))

print ("6)")
h=int(input("heigh:"))
treug = [[ 1  for j in range (i+1)]   for i in range (h)]
for i in range (h):
    for j in range (i+1):
        if j!=0 and j!=i and i>1:
            treug[i][j]=treug[i-1][j-1]+treug[i-1][j]
for i in treug:
    print (i)

print ("7)")

n=int(input("n:"))
list=list(range(2,n+1))
def simple_num (list):
    for i in list:
        if i>n**(1/2):
            break
            
        for j in list:
             if i!=j and j % i == 0:
                list.remove(j)
               
    return (list)
print (simple_num(list))








