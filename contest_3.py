def sorting(rr, s, e):
    if len(rr) > 1:
        middle = len(rr) // 2

        left = rr[:middle]
        right = rr[middle:]

        if len(rr) % 2 == 0:
            sorting(left, s, e-middle)
        else:
            sorting(left, s, e-middle-1)
        # sorting(left, s, e-middle-1)
        sorting(right, s+middle, e)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                rr[k] = left[i]
                i += 1
            else:
                rr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            rr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            rr[k] = right[j]
            j += 1
            k += 1
        print(f'{s} {e} {rr[0]} {rr[-1]}')
    return rr

n = int(input())
rrr = list(map(int, input().split(maxsplit=n)))
l_end = len(rrr)
print(*[i for i in sorting(rrr, 1, l_end)])