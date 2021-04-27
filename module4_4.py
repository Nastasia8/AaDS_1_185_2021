def find_min(n, k, el):
    stk = []
    for i in range(k):
        while stk and el[i] <= el[stk[-1]]:
            stk.pop()
        stk.append(i)

    for i in range(k, n):
        print(el[stk[0]])
        while stk and i - k >= stk[0]:
            stk.pop(0)
        while stk and el[i] <= el[stk[-1]]:
            stk.pop()
        stk.append(i)

    print(el[stk[0]])




n, k = map(int, input().split())
el = [int(i) for i in input().split()][:n[0]]
find_min(n, k, el)
