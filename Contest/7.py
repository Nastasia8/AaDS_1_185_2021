

def bucket_sort(arr, n):
    for i in range(n):
        bucket = [[] for i in range(10)]
        for j in arr: 
            el = int(j) // 10**i % 10
            bucket[el].append(j)
        if bucket[0] != arr:
            print_phase(bucket, i+1)
        arr = []
        for k in range(10):
            arr += bucket[k]
    return arr

def bucket_elements(bucket):
    string = ""
    for i in bucket:
        string += str(i)
        string += ", "
    return string[:-2]

def print_phase(bucket ,num=1):
    print("Phase", num)
    [print(f"Bucket {i}:", bucket_elements(bucket[i])) if bucket[i] else print(f"Bucket {i}: empty") for i in range(10)]
    print("**********")

#Input
n = int(input())
arr = []
for i in range(n):
    arr.append(input())
#Output
print("Initial array:")
print(bucket_elements(arr))
print("**********")
sorted_arr = bucket_sort(arr, n)
print("Sorted array:")
print(bucket_elements(sorted_arr))
