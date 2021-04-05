g = 1
a = int(input())
numbers = list(map(int, input().split(maxsplit = a)))
numbers.sort()
for i in range(1, a):
	if numbers[i-1] != numbers[i]:
		g +=1
print(g)