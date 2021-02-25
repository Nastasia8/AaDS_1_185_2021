n = int(input())
# arr = [[map(int, input().split())] for i in range(n)]
arr = []
for i in range(n):
    arr.append([])
    a, b = map(int, input().split())
    arr[i].append(a)
    arr[i].append(b)
k = -1

while k != 0:
    k = 0
    for i in range(len(arr)-1):
        if arr[i][1] < arr[i+1][1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            k += 1
k = -1
while k != 0:
    k = 0
    for i in range(len(arr)-1):
        if arr[i][1] == arr[i+1][1]:
            if arr[i][0] > arr[i+1][0]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                k += 1
for i in range(len(arr)):
    arr[i] = list(arr[i])
    print(arr[i][0], arr[i][1])
    # dict_ = {}
# for i in range(n):
#     a, b = map(int, input().split())
#     dict_[a] = b
# dict_ = {key: value for key, value in sorted(
#     dict_.items(), key=lambda item: item[1], reverse=True)}
# arr = list(dict_.items())
# arr.sort(key=lambda i: i[1], reverse=True)
