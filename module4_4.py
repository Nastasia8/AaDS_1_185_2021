from collections import deque
n = [int(i) for i in  input().split()]
s = deque([int(i) for i in input().split()][:n[0]])
m = 1e9 + 7
mins = []
while len(s) >= n[1]:
    for i in range(n[1]):
        if s[i] < m:
            m = s[i]
    mins.append(m)
    m = 1e9 + 7
    s.popleft()

[print(i) for i in mins]
