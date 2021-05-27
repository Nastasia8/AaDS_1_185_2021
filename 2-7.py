mass = []#создание пустого массива
length = int(input())
for i in range(length):#для данной длинны ввод элементов и добавление в массив
    mass.append(input())
print("Initial array:")
print(', '.join(mass))#вывод красивый
c = len(mass[0])
ph=0
r=10
for i in range(c-1,-1,-1):#перебор с конца с шагом -1
    ph+=1
    print('**********')
    print(f'Phase {ph}')# вывод номера коробки
    b = [[] for _ in range(r)]
    for j in range(len(mass)):
        b[ord(mass[j][i]) - ord('0')].append(mass[j])
    for j in range(r):
        if len(b[j])==0:
            print(f'Bucket {j}: empty')#вывод если пустой
        else:
            print("Bucket "+str(j)+": ", end='')
            for now in range(len(b[j])-1):
                print(b[j][now],end=', ')#
            print(b[j][len(b[j])-1])
    p = 0
    for j in range(r):# 
        for k in range(len(b[j])):
          mass[p] = b[j][k]
          p += 1
 
print('**********')
print("Sorted array:")#выводим сортированный массив
print(', '.join(mass))