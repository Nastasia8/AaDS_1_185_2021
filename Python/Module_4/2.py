import collections
from collections import deque
n = int(input())
list_a = list(map(int, input().split()))[:n]
list_a = collections.deque(list_a)
list_b = collections.deque()
list_dead_end = collections.deque()
list_result = collections.deque([i for i in range(1, n+1)])
while list_a:
    if not list_b or list_b[-1] > list_a[0]:
        list_b.append(list_a.popleft())
    if list_a:
        if list_b[-1] < list_a[0]:
            list_dead_end.append(list_b.pop())
while list_b:
    list_dead_end.append(list_b.pop())

if list_dead_end == list_result:
    print('YES')
else:
    print('NO')
