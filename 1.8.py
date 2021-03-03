def show_arr(arr):
    for i in arr:
        print(i)
def reverse_arr(arr):
    for i in arr:
        i.reverse()
        print(i)
arr = [[4, 3,5, 1], [0, 7, 2, 9], [2, 6, 3, 8]]
arr_= [[13, 97, 56], [17, 23, 85], [22, 45, 66]]
print("Исходная №1")
show_arr(arr)
print("#1")
arr1 = [i[::-1] for i in arr]
show_arr(arr1)
print("#2")
reverse_arr(arr)
#------------------------
print("Исходная №2")
show_arr(arr_)
print("#1")
arr_1 = [i[::-1] for i in arr_]
show_arr(arr_1)
print("#2")
reverse_arr(arr_)




