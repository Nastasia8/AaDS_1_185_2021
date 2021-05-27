count = 0

def mergeSort(numbers, start, end):
	if end - start > 1:
		middle = (start + end) // 2
		mergeSort(numbers, start, middle)
		mergeSort(numbers, middle, end)
		left = numbers[start: middle]
		right = numbers[middle: end]
		internalSort(numbers, left, right, start) 

def internalSort(arr, left, right, start):
	i = j = 0
	global count
	k = start
	while i < len(right) and j < len(left):
		if left[j] > right[i]:
			arr[k] = right[i]
			i += 1
			count += len(left) - j
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
	numbers = list(map(int, input().split(maxsplit = m)))
	mergeSort(numbers, 0, len(numbers))
	print(count)
	
main()