def f1(sp, invers):
    if len(sp) > 1:
        mid = len(sp)//2
        left = sp[:mid]
        right = sp[mid:]
        
        invers = f1(left, invers)
        invers = f1(right, invers)
        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sp[k] = left[i]
                i += 1
            else:
                sp[k] = right[j]
                j = j+1
                invers += len(left)-i
            k = k+1
        while i < len(left):
            sp[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            sp[k] = right[j]
            j = j+1
            k = k+1
    return invers
invers = 0
n = int(input())
sp = list(map(int, input().split()))
invers = f1(sp, invers)
print(invers)
