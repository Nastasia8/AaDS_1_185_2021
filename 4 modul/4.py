g,k=map(int,input().split())
nums = list(map(int,input().split(maxsplit=g)))
stack=[]
res=[0]*g
for i in range (g):
    while stack and nums[i]<nums[stack[-1]]:
        res[stack.pop()]=i
    stack.append(i)
while stack:

    res[stack.pop()]=g
i_m=0
for i in range (g-k+1):
    if i_m < i:
        i_m= i
    while res[i_m] < i+k:
        i_m= res[i_m]
    print (nums[i_m])