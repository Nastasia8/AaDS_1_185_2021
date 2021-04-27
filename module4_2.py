from collections import deque
n = int(input())
s = deque(list(map(int, input().split())))
dead_end = []
new_s = []
m = 1
while s:
    item = s.popleft()
    if m == item:
        new_s.append(item)
        m += 1
    elif len(dead_end) != 0:
        while dead_end:
            if m == dead_end[-1]:
                new_s.append(dead_end.pop())
                m += 1
            else:
                dead_end.append(item)
                break
        else:
            dead_end.append(item)
    else:
        dead_end.append(item)
while dead_end:
    item = dead_end.pop()
    if m == item:
        new_s.append(item)
        m += 1
    elif item > dead_end[-1]:
        break

if not s and not dead_end:
    print('YES')
else:
    print('NO')
