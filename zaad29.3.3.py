from collections import deque
n=int(input())
q1=deque()
q2=deque()
q3=deque()       
q4=deque()
for i in range(n):
    num,name=map(str, input().split())
    if int(num)==1:
        q1.append(name)
    if int(num)==2:
        q2.append(name)
    if int(num)==3:
        q3.append(name)
    else:
        q4.append(name)
while q1:
    print(1, q1.popleft())
while q2:
    print(1, q2.popleft())
while q3:
    print(1, q3.popleft())
while q2:
    print(1, q4.popleft())