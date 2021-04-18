def main():
    n = int(input())
    array = []
    i = 0
    while i <= (n - 1):
        array.append(int(input()))
        i += 1
    print("Initial array:")
    print(*array, sep = ", ")
    radixSort(array)
    print("**********")
    print("Sorted array:")
    print(*array, sep = ", ")


radixSort(array):
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
                print("Bucket", str(j) + ": ", sep = "", end = "")
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


