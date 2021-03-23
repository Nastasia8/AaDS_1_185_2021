def get_hash(s):
    p = 1e9 + 7
    x = 26
    res = 0
    for i in range(len(s)):
        res = (res*x+ord(s[i])) % p
    return res


s = str(input())
index_begin_1 = 1
index_end_2 = len(s)-1
flag = False
k = 0
while flag == False:
    # if s[index_begin:index_begin_1:1] == s[index_end_2:index_end:1] and s[index_begin:index_begin_1:1]*(len(s)//(k+1)) == s:
    #     flag = Trues
    if get_hash(s[0:index_begin_1:1]) == get_hash(s[index_end_2:len(s):1]) and s[0:index_begin_1:1]*(len(s)//(k+1)) == s:
        flag = True
    else:
        index_begin_1 += 1
        index_end_2 -= 1
    k += 1
print(len(s)//k)
