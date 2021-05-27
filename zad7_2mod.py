numbers = []
n = int(input())
for i in range(n):
    numbers.append(input())

print("Initial array:")
print(', '.join(numbers))

count=len(numbers[0])
Phase = 0
rang = 10
for i in range(count-1,-1,-1):
    Phase+=1
    print('**********')
    print(f'Phase {Phase}')
    bucket = [[] for _ in range(rang)]
    for j in range (len(numbers)):
        bucket [ord(numbers[j][i]) - ord('0')].append(numbers[j])
    for j in range(rang):
        if len(bucket[j])==0:
            print(f'Bucket {j}: empty')
        else:
            print("Bucket "+str(j)+": ", end='')
            for now in range(len(bucket[j])-1):
                print(bucket[j][now], end=', ')
            print(bucket[j][len(bucket[j])-1])
    p = 0
    for j in range (rang):
        for k in range (len(bucket[j])):
            numbers[p]= bucket[j][k]
            p+=1
print('**********')
print("Sorted array:")
print(', '.join(numbers))