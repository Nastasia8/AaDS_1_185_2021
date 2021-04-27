from collections import deque
from copy import copy
n = int(input())
list1 = deque(map(int, input().split()))
dead_end = deque()
list1_copy = copy(list1)

for i in list1_copy:
    dead_end.appendleft(i)
    if i == min(list1):
        list1.remove(i)
        dead_end.remove(i)
        dead_end_copy = copy(dead_end)
        for j in dead_end_copy:
            if j == min(list1):
                list1.remove(j)
                dead_end.remove(j)

            else: break
if dead_end:
    print("NO")
else:
    print("YES")