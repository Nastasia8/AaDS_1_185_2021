def prefix(s):
    dlina = len(s)
    k = [0] * dlina#создание массива нулей
    k[0] = 0
    for i in range(dlina - 1):#цикл до конца-1
        j = k[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = k[j - 1]
        if (s[i + 1] == s[j]):
            k[i+1] = j + 1
        else:
            k[i + 1] = 0
    return k

inp = str(input())
dlina = len(inp)#ввод данных
pref = prefix(inp)
for i in range(dlina - 1, dlina):#цикл в 
    res = dlina - pref[i]

if (dlina % res == 0):#если длина на результат делится без остатка, то делим, иначе выводим 1
    print(dlina // res)
else:
    print(1)