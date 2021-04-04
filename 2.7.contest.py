def bucket(spisok):
    new_buckets = [[] for i in range(10)]
    phase = 1
    while phase <= len(spisok[0]):
        for i in range(len(spisok)):
            f = spisok[i][len(spisok[i])-phase]
            bi = int(f)
            new_buckets[bi].append(spisok[i])
        print_phases(new_buckets, phase)
        phase += 1
        spisok = union(new_buckets)
        new_buckets = [[] for i in range(10)]
    else:
        print('**********\nSorted array:')
        print(print_stuff(spisok))
def union(lst):
    lst1 = []
    for i in lst:
        for j in i:
            lst1.append(j)
    return lst1

def print_stuff(arr):
    s = ''
    for i in arr:
        s += i + ', '
    return s[:-2]

def print_phases(new_buckets, phase):
    print(f'**********\nPhase {phase}')
    for i in range(10):
        if len(new_buckets[i]) == 0:
            print(f'Bucket {i}: empty')
        else:
            print(f'Bucket {i}: {print_stuff(new_buckets[i])}')

n = int(input())
spisok = [input() for i in range(n)]
print('Initial array:')
print(print_stuff(spisok))
bucket(spisok)
