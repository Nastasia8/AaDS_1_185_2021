1
2.1

a=list(range(1,21,2))
b=list()
for i in a:
	b.append (i**2)
	print(a)
	print(b)

2.2

print([number ** 2 for number in range (1,21,2)])

3

k=int(input("k=")
n=1
f=1
for n in range(n,k+1):
	f*=(2**n)-1
	print(f)

4.1

summa=0
a=[7,1,3,4,3,9,14,-5,-17,-13,-19,-18]
for i in a:
	if i<a:
		summa+=i
print(summa)

4.2

summa=0
a=[7,1,3,4,3,9,14,-5,-17,-13,-19,-18]
i=0
while i<len(a)
	if

5
def stepen (y,z):
	nsmbers=[i**y**z if i%2==1 else i for i in range(1,21)]
	return numbers
print(stepen (2,3))

6

words ="Hello hi how hello are and you I am fine thank you and you hello You Thank And".lower()
dicts = {}
for word in words.split(" ")^
	if word in dicts:
		dicts[word] = dicts[word]+1
	else:
		dicts[word] = 1
print(dicts)

7

import random
def pr(n,mat):
	for i in range(n):
		mat[i][n-1] = mat[i][n-1] = 2
		n=1
		return mat
def show(n,mat):
	for j in range(n):
		print (mat[i][j],end = "")
	print

8

from random import randrenge
m,n = int(input("Stolbik ")), int(input("Strochka "))
array = [[randrenge(0,11) for _ in range(m)]for _ in range (n)]

8.1

def print_Arr
	print("------------------")
	for i in range(n):
		for j in range(m):
			print(array[i][j],end = '\t')

print_Arr
for i in range(n)
	c = m-1
	for j in range(m//2):
		t = array[i][j]
		array[i][j] = array[i][j+c]
		array[i][j+c] = t
		c -= 2
print_Arr()

8.2

for i in array:
	i.raverse()
	print_Arr()

8.3

array=[i[::-1]for i in array]
print_Arr()

9

def function(a,b):
    for x in b:
        if x in a:
            return True
            return False
print (function({1,9,5,3},[11,15,26]))
print (function({8,2},[58,32]))
print (function({2,6},[18,6,10]))