from collections import deque

#1 3 2 4 5 3 1
data = list(map(int, input().split()))
n = data[0]
k = data[-1]
arr = list(map(int, input().split()))[:n]

def window_func(arr, window_width):
    window = deque([])
    for j in range(window_width):
        window.append(arr[j])
    for i in range(window_width, len(arr)+1):
        print(minimum)
        if i == len(arr):
            return
        window.popleft()
        window.append(arr[i])
window_func(arr, k)