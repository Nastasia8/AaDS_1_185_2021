# 1
# n = int(input('Кол-во чисел: '))
# a = []
# for i in range(n):
#     a.append(int(input(f"{i+1}-е число = ")))
# for i in range(len(a)):
#     if i == 0:
#         x, y = a[0], a[1]
#         while x != y:
#             if y > x:
#                 y -= x
#             else:
#                 x -= y
#         nod = x
#     elif i != 1:
#         x, y = nod, a[i]
#         while x != y:
#             if y > x:
#                 y -= x
#             else:
#                 x -= y
#         nod = x
# print(f'НОД = {nod}')
# 2
n = int(input('Кол-во чисел: '))
a = []
b_1 = []
b_2 = []
nod = 1
for i in range(n):
    a.append(int(input(f"{i+1}-е число = ")))
k = 2
for i in range(1, len(a)):
    if i == 1:
        while a[i] != 1:
            if a[i] % k == 0:
                a[i] = a[i] // k
                b_1.append(k)
            else:
                k += 1
        k = 2
        while a[i-1] != 1:
            if a[i-1] % k == 0:
                a[i-1] = a[i-1] // k
                b_2.append(k)
            else:
                k += 1
        k = 2
        set_b_1 = set(b_1)
        set_b_2 = set(b_2)
        sl_1 = {item: 0 for item in set_b_1}
        sl_2 = {item: 0 for item in set_b_2}
        for key in sl_1:
            for item in b_1:
                if item == key:
                    sl_1[key] += 1
        for key in sl_2:
            for item in b_2:
                if item == key:
                    sl_2[key] += 1
        for key_1 in sl_1:
            for key_2 in sl_2:
                if key_1 == key_2:
                    if sl_1[key_1] == sl_2[key_2]:
                        nod *= sl_1[key_1]*key_1
                    else:
                        if sl_1[key_1] > sl_2[key_2]:
                            nod *= sl_1[key_1]*key_2
                        else:
                            nod *= sl_1[key_1]*key_1  # я разложил на множители
                            # только превые два числа
    else:
        while a[i] != nod:
            if a[i] > nod:
                a[i] -= nod
            else:
                nod -= a[i]
print(nod)

# a = [1, 2, 2, 4, 1]
# b = set(a)
# sl = {item: 0 for item in b}
# for key in sl:
#     for item in a:
#         if key == item:
#             sl[key] += 1
