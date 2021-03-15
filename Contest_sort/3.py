def merge_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    print(c[0], c[len(c)-1])
    return c


def merge_sort(s, start, end):
    if end-start == 1:
        c = []
        c.append(s[start])
        return c
    middle = (end+start)//2
    left = merge_sort(s, start, middle)
    right = merge_sort(s, middle, end)
    print(start+1, end, end=" ")
    return merge_list(left, right)


n = int(input())
array = list(map(int, input(). split(maxsplit=n)))
result = merge_sort(array, 0, len(array))
print(*result)
