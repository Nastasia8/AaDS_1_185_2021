n = int(input())
list_ = input().split()
list_ = [int(list_[i]) for i in range(n)]
k = 0
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if list_[j] > list_[j+1]:
            list_[j], list_[j+1] = list_[j+1], list_[j]
            k += 1
            if k != 0:
                [print(i, end=" ") for i in list_]
                print('')
    if k == 0:
        print('0')
        break