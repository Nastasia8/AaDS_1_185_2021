def shift_down(value,heap):
    while 2*value+1<len(heap):
        left_indx=2*value+1
        right_indx=2*value+2
        _indx=left_indx
        if right_indx < len(heap) and heap[left_indx] > heap[right_indxx]:
            _indx=right_indx
        if heap[_indx]>=heap[value]:
            break
        heap[value],heap[_indx]=heap[_indx],heap[value]
        value=_indx
def shift_up(value,heap):
    while value>0 and heap[value]<heap[(value-1)//2]:
         heap[value], heap[(value-1) //2] = heap[(value-1)//2],heap[value]
         value=(value-1)//2
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
        if type(item)!=int:
            print(*item)
        else:
            print(item)
    print(*num)
main()