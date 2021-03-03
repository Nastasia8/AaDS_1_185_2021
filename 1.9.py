def serch(mn, sp):
    if mn == set(sp):
        return True
    else:
        return False

mn = {2, 8, 3, 9, 10, 1}
sp = [2, 3, 8, 9, 10, 10]
print(serch(mn, sp))