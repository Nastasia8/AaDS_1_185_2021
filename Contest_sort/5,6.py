#5

n=int(input())
numbers=list(map(int, input (). split (maxsplit=n)))
# print (len(set(numbers)))
k=1
numbers.sort()
for i in range (1,n):
    if numbers[i-1] != numbers [i]:
        k+=1
print (k)
    

#6

amount_staff=int(input())
staff=list(map(int, input (). split (maxsplit=amount_staff)))
amount_zakazov=int(input())
zakazi=list(map(int, input (). split (maxsplit=amount_zakazov)))
for i in range (amount_staff):
    if staff[i]<zakazi.count(i+1):
        print ("yes")
    else:
        print ("no")


