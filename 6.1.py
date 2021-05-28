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
    n, m = map(int, input().split()) 
    result = [] 
    num = [] 
    for i in range(m):
        commands = list(map(int, input().split())) 
        if commands[0] == 1: 
            if num: 
                if len(num) == 1: 
                    x = num.pop()
                    result.append([0, x]) 
                else:
                    num[0], num[-1] = num[-1], num[0]
                    x = num.pop()
                    result.append([shift_down(0, num), x]) 
            else:
                result.append(-1) 
        else: 
            if len(num) < n: 
                num.append(commands[1]) 
                result.append(shift_up(len(num)-1, num)) 
            else:
                result.append(-1) 
    for item in result: 
        if type(item) != int:
            print(*item)
        else:
            print(item)
    print(*num)
'''
1-20 функции shift up и down мы разбирали на паре, тут только +1 т.к. отсчет с 0
22-24 ввод данных
26 считывание комманды 
27-37 если 1 комманда ,рядовой куча не пустой, в куче 1 элемент то список 0 и элемент, иначе свап первого и последнего элементов, а результат из списка и элемента
иначе2 -1 по условию
38-43 2 комманда, если куча меньше заданной, +элемент, результат число после shift_up иначе -1
44-49 вывод