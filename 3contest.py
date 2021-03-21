def merge_sort(numbers,start,end):
  if end - start >1 :
    middle=(start+end)//2
    merge_sort(numbers,start,middle)
    merge_sort(numbers,middle,end)
    left=numbers[start:middle]
    right=numbers[middle:end]
    internal_sort(numbers,left,right,start)
    print(start+1,end,numbers[start],numbers[end-1])
def internal_sort(arr,left,right,start):
  i=j=0
  k=start
  while i <len(right) and j<len(left):
    if left[j]>right[i]:
      arr[k]=right[i]
      i+=1
    else:
      arr[k]=left[j]
      j+=1
    k+=1
  while i<len(right):
    arr[k]=right[i]
    i+=1
    k+=1
  while j<len(left):
    arr[k]=left[j]
    k+=1
    j+=1
  
n=int(input())
numbers=list(map(int, input().split()))
merge_sort(numbers,0,len(numbers))
print(*numbers)
