n = int(input())
list_ = input().split()
list_ = [int(list_[i]) for i in range(n)]

dict_ = {}
for i in list_:
    if i not in dict_:
        dict_[i] = 1
    elif i in dict_:
        dict_[i] += 1
print(len(dict_))