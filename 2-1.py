N=int(input())
s=input()
a=[]
k = 0
s=s.split(" ")
for i in range(N):
	a.append(int(s[i]))
for i in range (N-1):
	for j in range (N-i-1):
		if a[j] > a[j+1]:
			a[j], a[j+1]= a[j+1], a[j]
			k += 1
			print(*a, sep= " ")
if k == 0:
	print (0)