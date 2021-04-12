from collections import deque

#1 3 2 4 5 3 1
data = input()
n = int(data[0])
k = int(data[-1])
arr = list(map(int, input().split()))[:n]

def window_func(arr, window_width):
    window = deque([])

    for i in range(len(arr) - window_width+1):
        for j in range(i, i + window_width):
            window.append(arr[j])
        print(min(window))
        window.clear()

window_func(arr, k)