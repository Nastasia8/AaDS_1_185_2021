from collections import deque
n,k= map(int,input().split())
nums=list(map(int,input().split()))
deq=deque()
for i in range(k):
  while deq and nums[i] <nums[deq[-1]]:
    deq.pop()
  deq.append(i)
print(nums[deq[0]])
for i in range(k,n):
  while deq and deq[0] <=i-k:
    deq.popleft()
  while deq and nums[i] <= nums[deq[-1]]:
    deq.pop()
  deq.append(i)
  print(nums[deq[0]])
