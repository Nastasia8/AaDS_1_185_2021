#4
def merge_sort(arr):
    global count
    if len(arr) > 1:
        middle = len(arr) // 2
        half1 = arr[:middle]
        half2 = arr[middle:]
        merge_sort(half1)
        merge_sort(half2)
        i = 0
        j = 0
        k = 0
        while i < len(half1) and j < len(half2):
            if half1[i] > half2[j]:
                arr[k] = half2[j]
                j += 1
                count += len(half1) - i
            else:
                arr[k] = half1[i]
                i += 1
            k += 1

        while i < len(half1):
            arr[k] = half1[i]
            k += 1
            i += 1
            
        while j < len(half2):
            arr[k] = half2[j]
            k += 1
            j += 1
    return arr

n = int(input())
arr = list(map(int, input().split()))[:n]
count = 0
merge_sort(arr)
print(count)
#7
n=int(input())
print("Initial array:")
Massive=[]
[Massive.append(input()) for _ in range (n)]

for i in range(len(Massive)-1):
    print(Massive[i], end=", ")
print(Massive[len(Massive)-1])
faza = 0
m = len(Massive[0])
for i in range(m-1,-1,-1):
    print("**********")
    faza += 1
    print("Phase",faza)
    bucket = [[] for _ in range(10)]
    for j in range(len(Massive)):
        bucket[ord(Massive[j][i]) - ord("0")].append(Massive[j])
    for j in range(10):
        if len(bucket[j])==0:
            print("Bucket ",str(j),": empty",sep="")
        else:
            print("Bucket ",str(j),": ",sep="", end="")
            for k in range(len(bucket[j])-1):
                print(bucket[j][k],end=", ")
            print(bucket[j][len(bucket[j])-1])
    p = 0
    for j in range(10):
        for k in range(len(bucket[j])):
            Massive[p] = bucket[j][k]
            p += 1
print("**********")
print("Sorted array:")
for i in range(len(Massive)-1):
    print(Massive[i], end=", ")
print(Massive[len(Massive)-1])
