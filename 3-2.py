def sdvig(s, t, q):
    if s==t:
        return 0# если равны возвращаем 0
    else:
        t*=2#иначе проходим алгоритм хеширования
        p = 11#простое число
        m = 1
        sh = 0
        for i in s[::-1]:#идём в обратном направлении
            sh += ord(i) * m
            m *= p
            sh %= q
            m %= q

        m = 1
        hash = 0
        for i in t[:len(s)][::-1]:
            hash += m * ord(i)#значению предыдущего хеша добавляем следующий
            m *= p
            hash %= q
            m %= q

        ht = 1
        for i in range(len(s) - 1):#цикл до конца-1, чтоб не выйти за границы
            ht *= p
            ht %= q
        for i in range(1, len(t) - len(s) + 1):
            hn = ((hash % q - ord(t[i - 1]) * ht % q) * p % q + ord(t[i + len(s) - 1])) % q
            if hn == sh:#если строки равны возвращаем индекс, где равны
                return i
            hash = hn

        return -1

s = input()
t = input()#ввод строк
q = 2**31 - 1#константа
print(sdvig(s,t,q))#вывод