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

2

if l==0:
    print(0)

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


7