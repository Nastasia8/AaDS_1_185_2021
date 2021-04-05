модуль 2


1


n=int(input())
a = list(map(int, input().split(maxsplit=n)))
l = 0
i = 0
for i in range(n-1):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            l =1
            print(*a, sep=" ")

if l==0:
    print(0)


2


n = int(input())
a = []
for i in range(n):
	a.append(list(map(int,input().split())))


a.sort(key = lambda x: x[0])
a.sort(key = lambda x: x[1], reverse = True)
for i in a:
	for b in i:
		print(b,end = ' ')
	print()


3


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


5


n = int(input())
print(len(set(list(map(int,input().split()))[:n])))


6


articles = int(input())
article_amount = list(map(int,input().split()))[:articles]

clients = int(input())
client_orders = list(map(int,input().split()))[:clients]

for i in range(articles):
    if article_amount[i] < client_orders.count(i + 1):
        print('yes')
    else: 
        print('no')


модуль 3


1


def prefix(s):
    p=[0]*len(s)
    for i in range(len(s)-1):
        j=p[i]
        while j>0 and s[j]!=s[i+1]:
            j=p[j-1]
        if s[j]==s[i+1]:
            p[i+1]=j+1
        else:
            p[i+1]=0
    return p
    
def main():
    s=input()
    t=input()
    p=prefix(t+"*"+s)
    for i in range(len(p)):
        if p[i]==len(t):
            print(i-2*len(t), end=" ")

main()