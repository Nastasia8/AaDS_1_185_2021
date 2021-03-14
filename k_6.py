n = int(input())
c = list(map(int, input().split(maxsplit = n)))
k = int(input())
p = list(map(int, input().split(maxsplit = k)))

t = [0]*101
for i in p:
	t[i] += 1
for i in range(n):
	if t[i+1] > c[i]:
		print('yes')
	else:
		print('no')