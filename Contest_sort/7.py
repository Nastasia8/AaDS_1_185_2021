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