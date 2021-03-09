N = int(input())
a = []
text = input()
b=0
a = [int(num) for num in text.split()]
for i in range(N-1):
    for j in range(N-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            print(*a, sep=" ")
            b+=1
if b==0:
  print(0)
