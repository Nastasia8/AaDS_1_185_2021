def prime(k):
    i = 2
    count = 0
    for i in range(1,k+1):
        if(k%i == 0):
            count = count+1
    if(count == 2):
        return True
    else:
        return False


def sumprimes(list_):
    result = []
    for x in list_:
        if prime(x):
            result.append(x)
    return result

k = int(input())
list_ = [i for i in range(1, k)]

print(sumprimes(list_))