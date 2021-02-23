def func(k):
    list_ = [i for i in range(1, k)]
    for i in list_:
        for j in range(1, len(list_)):
            value = list_[j+1]
            print(value)
            if type(value) != int:
                pass
            elif value == list_[-1]:
                if value % i == 0:
                    list_[j+1] = ""

            elif value % i == 0:
                list_[j+1] = ""
            # if type(j) != int:
            #     pass
            # elif list_[j] == list_[-1]:
            #     if list_[j] % i == 0:
            #         list[list_.index(j)] = ""
            #     return list_
            # elif list_[j] % i == 0:
            #     list_[list_.index(j)] = ""
            # print(i)
            # print(j)
    return list_

print(func(10))
