def count_changes(r4):
    return merge(r4)[1]

def merge(r4):
    if len(r4) <= 1:
        return r4, 0
    middle = int( len(r4) / 2 )
    left_side, a = merge(r4[:middle])
    right_side, b = merge(r4[middle:])
    result, c = merge2(left_side, right_side)
    return result, (a + b + c)

def merge2(l, r):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(l)
    while i < left_len and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            count += left_len - i
            j += 1
    result += l[i:]
    result += r[j:]
    return result, count
n = int(input())
rrr = list(map(int, input().split(maxsplit=n)))
print(count_changes(rrr))

