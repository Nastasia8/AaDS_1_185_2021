#1
N = int(input())
a = list(map(int,input().split(maxsplit=N)))
y = [i for i in a]

i = 0
while i < N- 1:
    j = 0
    while j < N - 1 - i:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print (*a, sep = "  ")
        j += 1
    i += 1
if y == a:
    print(0)
#2
q = int(input())
a = []
for i in range(q):
	a.append(list(map(int,input().split())))
a.sort(key = lambda x: x[0])
a.sort(key = lambda x: x[1], reverse = True)
for i in a:
	for b in i:
		print(b,end = ' ')
	print()
#3
def mergeSort(numbers, start, end):
	if end - start > 1:
		middle = (start + end) // 2
		mergeSort(numbers, start, middle)
		mergeSort(numbers, middle, end)
		left = numbers[start: middle]
		right = numbers[middle: end]
		internalSort(numbers, left, right, start)
		print(start + 1, end, numbers[start], numbers[end - 1])

def internalSort(arr, left, right, start):
	i = j = 0
	k = start
	while i < len(right) and j < len(left):
		if left[j] > right[i]:
			arr[k] = right[i]
			i +=1
		else:
			arr[k] = left[j]
			j += 1
		k += 1
	while j < len(left):
		arr[k] = left[j]
		j += 1
		k += 1
	while i < len(right):
		arr[k] = right[i]
		i += 1
		k += 1

def main():
	m = int(input())
	numbers = list(map(int,input().split(maxsplit = m)))
	mergeSort(numbers, 0, len(numbers))
	print(*numbers)

main()
#5
x = int(input())
y = input().split()[:x]

print(len(set(y)))
#6
x = int(input())
c = list(map(int, input().split(maxsplit = x)))
y = int(input())
p = list(map(int, input().split(maxsplit = y)))

z = [0]*101
for i in p:
	z[i] += 1
for i in range(x):
	if z[i+1] > c[i]:
		print('yes')
	else:
		print('no')