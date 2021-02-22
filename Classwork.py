words = "Bass, Pike, Roach, Catfish, Trout, Mackerel, Salmon, Zander, Anchovy".split(", ")
'''
new_list=[]
for word in words:
    new_list.append(word[-1])
print(sorted(new_list, reverse=True))

print(sorted([word[-1] for word in words ], reverse=True)) 
a=list(map(lambda word:word[-1],words))
a.sort(reverse=True)
print(a) 

print(list(map(lambda n:n+2, filter(lambda m:m%2==1, range(1,21)))))

a=[1,4,5,6,7,4,3,3,7,0,3]
b=3
l=list()
for i in range(len(a)):
     if a[i]==b:
        l.append(i)
print(l)

a=[1,4,5,6,7,4,3,3,7,0,3]
print([i for i,item in enumerate(a) if item==7])
'''
list1=list(range(1,20,2))
def funk(list1,y,z):
  new_list=[]
  for i in list1:
    if i%2!=0:
       new_list.append((i**y)**z)
  return  new_list
 new_list=funk(list1,3,2)
print(new_list)