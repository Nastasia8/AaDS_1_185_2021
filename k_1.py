N = int(input())
numbers = input().split()
numbers = [int(i) for i in numbers]
b = 0
for i in range(N-1):
	for j in range(N-i-1):
		if numbers[j] > numbers[j+1]:
			numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
			print(" ".join(map(str, numbers)))
			b += 1
if b == 0:
    print(0)
