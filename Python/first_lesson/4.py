arr = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
s = 0
s2 = 0
for item in arr:
    if item < 0:
        s += item
x = 0
while (x != len(arr)):
    if arr[x] < 0:
        s2 += arr[x]
    x += 1
print(s)
print(s2)
