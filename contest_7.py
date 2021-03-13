def bucket_s(rrr):
    new_buckets = [[] for i in range(10)]
    phase = 1
    while phase <= len(rrr[0]):
        for i in range(len(rrr)):
            f = rrr[i][len(rrr[i])-phase]
            bi = int(f)
            new_buckets[bi].append(rrr[i])
        print_phases(new_buckets, phase)
        phase += 1
        rrr = union(new_buckets)
        new_buckets = [[] for i in range(10)]
    else:
        print('**********\nSorted array:')
        print(print_stuff(rrr))


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
rrr = [input() for i in range(n)]
print('Initial array:')
print(print_stuff(rrr))
bucket_s(rrr)