from collections import Counter
n=input()
arr = list(map(int, input().split()))
k=input()
pr = Counter(map(int, input().split()))
[print('yes' if arr[i - 1] - pr[i] < 0 else 'no') for i in range(1, len(arr) + 1)]