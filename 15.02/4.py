list_ = [5, 6, 9, 6, 3, 5, 2, 5, 1]

def func(set_):
    new_set = {}
    for i in range(len(set_)):
        el = set_[i]

        if el in new_set:
            new_set[el] = new_set[el] + 1
            set_[i] = str(el) * new_set[el]
            
        elif i not in new_set:
            new_set[el] = 1
    return set_

print(func(list_))


