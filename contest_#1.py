n = int(input())
s = input().split()
s_ = [int(s[x]) for x in range(n)]
c = 0
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if s_[j] > s_[j+1]:
            c += 1
            s_[j], s_[j+1] = s_[j+1], s_[j]
            print(*[str(s_[f]) for f in range(n)])
    if c == 0:
        print(0)
        break