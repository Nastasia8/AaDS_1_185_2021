def func(number):
    list_ = []
    while number != 1:
        if number % 2 == 0:
            number /= 2
            list_.append(int(number))
        else:
            number = ((number*3) + 1) / 2
            list_.append(int(number))
    return list_

num = int(input())
print(func(num))