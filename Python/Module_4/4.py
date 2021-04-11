from collections import defaultdict, deque


def min_value(arr, min_index):
    if min_index == 0:
        min_v = arr[0]
        for i in range(len(arr)):
            if arr[i] < min_v:
                min_v = arr[i]
                min_index = i
        print(min_v)
    elif arr[-1] < arr[min_index - 1]:
        print(arr[-1])
    else:
        print(arr[min_index-1])
    return min_index


n, k = map(int, input().split())
num = deque(list(map(int, input().split()))[:n])
queue = deque([])
min_index = 0
for i in range(k):
    queue.append(num.popleft())


while num:
    min_index = min_value(queue, min_index)

    queue.popleft()
    queue.append(num.popleft())

min_index = min_value(queue, min_index)
