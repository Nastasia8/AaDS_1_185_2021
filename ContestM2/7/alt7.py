

def bucket_sort(arr):
    bucket = [[] for i in range(10)]
    phases = 1
    while phases <= len(arr[0]):
        for i in range(len(arr)):
            el = int(arr[i][len(arr[i])-phases])
            bucket[el].append(arr[i])
        print_phase(bucket, phases)
        phases += 1
        arr = []
        for k in range(10):
            arr += bucket[k]
        bucket = [[] for i in range(10)]

    print('Sorted array:')
    print(bucket_elements(arr))


def print_phase(bucket, i):
    print("Phase", i)
    [print(f"Bucket {s}:", bucket_elements(bucket[s])) 
    if bucket[s] else print(f"Bucket {s}: empty") for s in range(10)]
    print("**********")


def bucket_elements(bucket):
    string = ""
    for i in bucket:
        string += str(i)
        string += ", "
    return string[:-2]

def main_func():
    #Input
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    #Output
    print("Initial array:")
    print(bucket_elements(arr))
    print("**********")
    bucket_sort(arr)

if __name__ == "__main__":
    main_func()