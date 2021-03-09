n=int(input())
sp=[]
for i in range(n):
	sp.append(input().split())
sp=[[int(sp[i][j]) for j in range(2)]for i in range(n)]
for i in range(n-1):
	for j in range(n-i-1):
		if sp[j][1]<sp[j+1][1]:
			t=sp[j]
			sp[j]=sp[j+1]
			sp[j+1]=t
		if sp[j][1]==sp[j+1][1]:
			if sp[j][0]>sp[j+1][0]:
				t=sp[j]
				sp[j]=sp[j+1]
				sp[j+1]=t
[print(i[0],i[1]) for i in sp]
