n,k=map(int,input().split())
nums = list(map(int,input().split(maxsplit=n)))
stack=[]
res=[0]*n
for i in range (n):
    while stack and nums[i]<nums[stack[-1]]:
        res[stack.pop()]=i
    stack.append(i)
while stack:
    res[stack.pop()]=n


i_m=0
for i in range (n-k+1):
    if i_m < i:
        i_m= i
    while res[i_m] < i+k:
        i_m= res[i_m]
    print (nums[i_m])