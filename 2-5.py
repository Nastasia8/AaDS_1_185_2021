def merge(l_list, r_list):# функция сортировки принимает левую и правую части
    s_list = []# создаем список
    l_idx = 0
    r_idx = 0
    for i in range(len(l_list)+len(r_list)):# цикл до суммы 2х частей
        if l_idx < len(l_list) and r_idx < len(r_list):
            if l_list[l_idx] <= r_list[r_idx]:#если элемент меньше
                s_list.append(l_list[l_idx])# то добавляем в список
                l_idx += 1               
            else:
                s_list.append(r_list[r_idx])# иначе добавляем другой элемент
                r_idx += 1                
    s_list += l_list[l_idx:]
    s_list += r_list[r_idx:]
    return s_list# возвращение списка


def merge_sort(uns_list):#сортировка как в других заданиях
    if len(uns_list) == 1:
        return uns_list
    mid = len(uns_list) // 2
    l_list = merge_sort(uns_list[:mid])# в список передаём результат функции до середины
    r_list = merge_sort(uns_list[mid:])# тоже, но после сердины
    return merge(l_list, r_list)


n = int(input())
stroka = list(map(int, input().split()))#ввод списка 
stroka = merge_sort(stroka)
for i in range(1, len(stroka)):# если при проходе строки предыдущий и текущий элементы равны, то из н вычитаем 1
    if stroka[i]==stroka[i-1]:
        n-=1
print(n)