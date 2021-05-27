string1 = input()
string2 = input()#ввод строк
res = []
for i in range(len(string2), len(string1)+1):#простой обход по строкам и проверка совпадений
    if string2 == string1[i-len(string2):i]:
        res.append(i-len(string2))
print(" ".join(map(str,res)))#красивый вывод