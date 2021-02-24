n = int(input('n = '))
a = str(input('a: '))
for i in range(n):
    for x in range(i+1):
        print(a, end='')
    print(' ')

print('----------------------')
for i in range(n)[::-1]:
    for x in range(i+1):
        print(a, end='')
    print(' ')
print('-----------------------')
print('-----------------------')
n_2 = n
while n != 0:
    for x in range(n):
        print(a, end='')
    print(' ')
    n -= 1
print('------------------------')
while n != n_2+1:
    for x in range(n):
        print(a, end='')
    print(' ')
    n += 1
