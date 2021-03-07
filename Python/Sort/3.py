"""
>>> import io, sys
>>> sys.stdin = io.StringIO(chr(10).join(['5', '5 4 3 2 1']))
>>> merge_sort_main()
1 2 4 5
4 5 1 2
3 5 1 3
1 5 1 5
1 2 3 4 5 
"""


def merge_sort_main():
    n = int(input())
    arr = list(map(int, input().split()))[:n]

    def merge_sort(arr, begin_, end_):
        k = len(arr)
        if k > 2:
            if k % 2 == 0:
                left = merge_sort(arr[:k//2], begin_, end_-k//2)
            else:
                left = merge_sort(arr[:k//2], begin_, end_-k//2-1)
            if k % 2 == 0:
                right = merge_sort(arr[k//2:], begin_+k//2, end_)
            else:
                right = merge_sort(arr[k//2:], begin_+k//2, end_)
            # right = merge_sort(arr[k//2:], (k//2)+1, k)
            # print(arr)
            arr = left + right
            last_index = len(arr) - 1
            for i in range(last_index):
                min_value = arr[i]
                min_index = i
                for j in range(i+1, last_index + 1):
                    if min_value > arr[j]:
                        min_value = arr[j]
                        min_index = j
                        if min_index != i:
                            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(begin_, end_, arr[0], arr[-1])

        elif k > 1 and arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            print(begin_, end_, arr[0], arr[1])
            # print(arr)

        return arr

    # merge_sort(arr, 1, len(arr))
    arr = merge_sort(arr, 1, len(arr))
    [print(item, end=" ") for item in arr]


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)
merge_sort_main()

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr)//2
#         left = arr[:mid]
#         right = arr[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         r, l, k = 0, 0, 0
#         while r < len(right) and l < len(left):
#             if right[r] < left[l]:
#                 arr[k] = right[r]
#                 r += 1
#             else:
#                 arr[k] = left[l]
#                 l += 1
#             k += 1
#         while l < len(left):
#             arr[k] = left[l]
#             k += 1
#             l += 1
#         while r < len(right):
#             arr[k] = right[r]
#             k += 1
#             r += 1
#         print(arr)
#     return arr


# merge_sort(arr)
# [print(item, end=' ')for item in arr]
