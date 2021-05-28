n = int(input())
a = list(map(int, input().split(maxsplit = n)))
s = 1
a.sort()
for i in range(n - 1):
	if a[i] != a[i + 1]:
		s += 1
print(s)