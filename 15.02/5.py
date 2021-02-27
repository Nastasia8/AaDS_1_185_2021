def main(list1_):
    list2_ = []
    tuple_ = ()
    for i in list1_:
        if i in list2_:
            pass
        else:
            list2_.append(i)
    list2_.sort()
    tuple_ = list2_.copy()
    return tuple_
#just enter with single string
list_ = [int(i) for i in input()]
print(main(list_))