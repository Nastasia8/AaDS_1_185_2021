def xxx(mn, arr):
    for item in arr:
        if item not in mn:
            return False
    return True


mn = {1, 5, 'color', 2}
arr = [1, 5]
arr_2 = [3, 1, 5, 'color']
print(xxx(mn, arr))
print(xxx(mn, arr_2))
