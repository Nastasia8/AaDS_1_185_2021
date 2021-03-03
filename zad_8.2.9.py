def Function(a,b): #a-множество b-список
    for i in b:
        if i in a:
            return True
    return False

print(Function({1,2},[5]))
print(Function({1,2},[1,2,3]))
print(Function({1,2},[1,3]))