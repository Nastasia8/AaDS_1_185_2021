def merge(l_list, r_list, str_idx, end_idx):
    s_list = []
    l_idx = 0
    r_idx = 0
    for i in range(len(l_list)+len(r_list)):#для и меньше суммы правого и левого листа
        if l_idx < len(l_list) and r_idx < len(r_list):# если можно ещё делить
            if l_list[l_idx] <= r_list[r_idx]:
                s_list.append(l_list[l_idx])#добавление в список
                l_idx += 1               
            else:
                s_list.append(r_list[r_idx])
                r_idx += 1                
    s_list += l_list[l_idx:]
    s_list += r_list[r_idx:]
    print(str(str_idx)+" "+str(end_idx)+" "+str(s_list[0])+" "+str(s_list[-1]))
    return s_list# возвращаем часть списка
def m_sort(uns_list, str_idx, end_idx):
    if len(uns_list) == 1:# если длина 1, то вернём сам элемент
        return uns_list
    mid = len(uns_list) // 2# делим пополам
    l_list = m_sort(uns_list[:mid], str_idx, str_idx + mid-1)#сортировка левой части
    r_list = m_sort(uns_list[mid:], str_idx + mid, end_idx)#сортировка правой части
    return merge(l_list, r_list, str_idx, end_idx)
n = int(input())# ввод количества элементов
stroka = list(map(int, input().split()))#вводим элементы в список
stroka = m_sort(stroka, 1, len(stroka))# присваиваем отсортированный список
print(" ".join(map(str, stroka)))#выводим список без запятых и скобок
