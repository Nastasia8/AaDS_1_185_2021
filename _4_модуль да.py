#1
#s = input()
#k = 0
#stack = []
#for i in s:
#    if i==")":
#        if stack:
#            stack.pop()
#            k+=2
#    else:
#        stack.append(i)
#print(len(s) - k)
#2
#n = int(input())
#string = list(map(int, input().split()))
#stack = []
#isPsk = True
#num = 1
#for i in string:
#    for j in range(len(stack)):
#        if stack and num == stack[-1]:
#            stack.pop()
#            num += 1
#    if i != num:
#        if stack and i > stack[-1]:
#            isPsk = False
#            break
#        stack.append(i)
#    else:
#        num += 1
#if isPsk:
#    print ("YES")
#else:
#    print ("NO")
#3
#n = int(input())
#nums = list(map(int,input().split()))[:n]
#d = {i:nums[i] for i in range (n)}
#stack = []
#index = [0]*n
#for i in range(n-1,-1,-1):
#    while stack and stack[-1][1] >= d[i]:
#        stack.pop()
#    if not stack:
#        index[i] = -1
#    else:
#        index[i] = stack[-1][0]
#    stack.append([i, d[i]])
#print(*index)    
#4
#n, k = map(int, input().split())
#nums = list(map(int, input().split()))
#stack = []
#res = [0] * n
#for i in range(n):
#    while stack and nums[i] < nums[stack[-1]]:
#        res[stack.pop()] = i
#    stack.append(i)
#while stack:
#    res[stack.pop()] = n
#i_n = 0
#for i in range(n - k + 1):
#    if i_n < i:
#        i_n = i
#    while res[i_n] < i + k:
#        i_n = res[i_n]
#    print(nums[i_n])