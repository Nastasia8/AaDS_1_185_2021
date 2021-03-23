s = str(input())
index_begin = 0
index_begin_1 = 1
index_end = len(s)
index_end_2 = len(s)-1
flag = False
k = 0
while flag == False:
    if s[index_begin:index_begin_1:1] == s[index_end_2:index_end:1]:
        flag = True
    else:
        index_begin_1 += 1
        index_end_2 -= 1
    k += 1
print(len(s)//k)
