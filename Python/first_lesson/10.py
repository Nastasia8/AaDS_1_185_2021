arr = [6, 43, -2, 11, -55, -12, 3, 345, 0]
d = {arr[i]: 'positive' if arr[i] > 0 else 'negative' if arr[i]
     < 0 else 'zero' for i in range(len(arr))}
print(d)
