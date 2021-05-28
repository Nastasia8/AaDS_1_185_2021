#фукнции shift_up, shift_down разбирали на паре, только тут возвращают индекс +1 тк с 0 шел отсчет
def shift_up(cur_index, heap):
    while heap[cur_index] > heap[(cur_index-1)//2] and (cur_index-1)//2 >= 0:
        heap[cur_index], heap[(cur_index-1) //2] = heap[(cur_index-1)//2], heap[cur_index]
        cur_index = (cur_index-1)//2
    return cur_index+1


def shift_down(cur_index, heap):
    while 2*cur_index+1 < len(heap):
        left_cur_index = 2*cur_index+1
        right_cur_index = 2*cur_index+2
        child_index = left_cur_index
        if right_cur_index < len(heap) and heap[left_cur_index] < heap[right_cur_index]:
            child_index = right_cur_index
        if heap[child_index] <= heap[cur_index]:
            break
        heap[child_index], heap[cur_index] = heap[cur_index], heap[child_index]
        cur_index = child_index
    return cur_index+1

def main():
    n, m = map(int, input().split()) #ввод n и m
    result = [] #создание конечного списка
    num = [] # список для счета
    for i in range(m):
        commands = list(map(int, input().split())) #считывание команды
        if commands[0] == 1: #Если 1-я команда
            if num: # если куча не пустая
                if len(num) == 1: # если в кучеодин элемент
                    x = num.pop()
                    result.append([0, x]) #в конечном результате список из 0(по условию) и элементу
                else:
                    num[0], num[-1] = num[-1], num[0] #иначе куча меняет первый и последний элемент местами
                    x = num.pop()
                    result.append([shift_down(0, num), x]) # в резульате список из индекса и элемента
            else:
                result.append(-1) # иначе -1 (по условтю)
        else: # если 2-я команда
            if len(num) < n: #если куча меньше заданной границы
                num.append(commands[1]) # добавляем элемент
                result.append(shift_up(len(num)-1, num)) # в результат число после функции shift_up
            else:
                result.append(-1) # иначе -1 (по условию)
    for item in result: # вывод кучи учитывая тип данных
        if type(item) != int:
            print(*item)
        else:
            print(item)
    print(*num)


main()