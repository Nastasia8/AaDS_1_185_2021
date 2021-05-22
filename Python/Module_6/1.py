def shift_up(cur_index, heap):
    while heap[cur_index] > heap[(cur_index-1)//2] and (cur_index-1)//2 >= 0:
        heap[cur_index], heap[(cur_index-1) //
                              2] = heap[(cur_index-1)//2], heap[cur_index]
        cur_index = (cur_index-1)//2
    # print(cur_index+1)
    return cur_index+1


def shift_down(cur_index, heap):
    while 2*cur_index+1 < len(heap):
        left_cur_index = 2*cur_index+1
        right_cur_index = 2*cur_index+2
        child_index = left_cur_index
        if right_cur_index < len(heap) and heap[left_cur_index] > heap[right_cur_index]:
            child_index = right_cur_index
        if heap[child_index] <= heap[cur_index]:
            break
        heap[child_index], heap[cur_index] = heap[cur_index], heap[child_index]
        cur_index = child_index
    # print(cur_index+1, end=" ")
    return cur_index+1


def main():
    n, m = map(int, input().split())
    result = []
    num = []
    for i in range(m):
        a = list(map(int, input().split()))
        if a[0] == 1:
            if num:
                if len(num) == 1:
                    num.pop()
                    result.append(0)
                else:
                    num[0], num[-1] = num[-1], num[0]
                    x = num.pop()
                    result.append([shift_down(0, num), x])
            else:
                result.append(-1)
        else:
            if len(num) < n:
                num.append(a[1])
                result.append(shift_up(len(num)-1, num))
            else:
                result.append(-1)
    for item in result:
        if type(item) != int:
            print(*item)
        else:
            print(item)
    print(*num)


main()
