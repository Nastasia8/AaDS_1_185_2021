def triangle(h):
    f_list = [1, 1]
    s_list = [1, 1]
    print([1])
    k = 1
    for i in range(h-1):
        for j in range(1, k):
            s_list[j] = f_list[j-1] + f_list[j]
            if j == k-1:
                s_list.append(1)
        print(s_list)
        k += 1
        f_list = s_list.copy()
triangle(6)