n = int(input())
list_ = []
for i in range(n):
    id_, value = map(int, input().split())
    list_.append([id_, value])
for i in range(n-1):
    for j in range(n-i-1):
        if list_[j][1] < list_[j+1][1]:
            list_[j], list_[j+1] = list_[j+1], list_[j]
        if list_[j][1] == list_[j+1][1]:
            if list_[j][0] > list_[j+1][0]:
                list_[j], list_[j+1] = list_[j+1], list_[j]
[print(i[0], i[1]) for i in list_]