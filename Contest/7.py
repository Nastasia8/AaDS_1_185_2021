#This working faster, but make mistakes

def bucket_sort(arr, n):
    for i in range(n+1):
        bucket = [[] for i in range(10)]
        for j in arr:
            el = int(j) // 10**i % 10
            bucket[el].append(j)
        if bucket[0] != arr:
            print("Phase", i+1)
            [print(f"Bucket {s}:", bucket_elements(bucket[s])) if bucket[s] else print(f"Bucket {s}: empty") for s in range(10)]
            print("**********")
            arr = []
            for k in range(10):
                arr += bucket[k]
        
    print("Sorted array:")
    print(bucket_elements(arr))

def bucket_elements(bucket):
    string = ""
    for i in bucket:
        string += str(i)
        string += ", "
    return string[:-2]

#Input
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
#Output
print("Initial array:")
print(bucket_elements(arr))
print("**********")
bucket_sort(arr, n)