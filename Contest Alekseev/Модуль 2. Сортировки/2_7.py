def main():
    n = int(input())
    array = []
    i = 0
    while i <= (n - 1):
        array.append(input())
        i += 1
    print("Initial array:")
    print(*array, sep = ", ")
    radixSort(array)
    print("**********")
    print("Sorted array:")
    print(*array, sep = ", ")

def radixSort(array):
    phase = 0
    m = len(array[0])
    for i in range(m - 1, -1, -1):
        print("**********")
        phase += 1
        print("Phase", phase)
        bucket = [[] for _ in range(10)]
        for j in range(len(array)):
            bucket[ord(array[j][i]) - ord("0")].append(array[j])
        for j in range(10):
            if len(bucket[j]) == 0:
                print("Bucket", str(j) + ": empty")
            else:
                print("Bucket ", str(j) + ": ", sep = "", end = "")
                for k in range(len(bucket[j]) - 1):
                    print(bucket[j][k], end = ", ")
                print(bucket[j][len(bucket[j]) - 1])
        p = 0
        for j in range(10):
            for k in range(len(bucket[j])):
                array[p] = bucket[j][k]
                p += 1
    return array

main()

'''
9
12
32
45
67
98
29
61
35
09
'''

'''
Initial array:
12, 32, 45, 67, 98, 29, 61, 35, 09
**********
Phase 1
Bucket 0: empty
Bucket 1: 61
Bucket 2: 12, 32
Bucket 3: empty
Bucket 4: empty
Bucket 5: 45, 35
Bucket 6: empty
Bucket 7: 67
Bucket 8: 98
Bucket 9: 29, 09
**********
Phase 2
Bucket 0: 09
Bucket 1: 12
Bucket 2: 29
Bucket 3: 32, 35
Bucket 4: 45
Bucket 5: empty
Bucket 6: 61, 67
Bucket 7: empty
Bucket 8: empty
Bucket 9: 98
**********
Sorted array:
09, 12, 29, 32, 35, 45, 61, 67, 98
'''
