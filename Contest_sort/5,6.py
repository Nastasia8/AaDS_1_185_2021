#5

n=int(input())
numbers=list(map(int, input (). split (maxsplit=n)))
print (len(set(numbers)))

#5

amount_staff=int(input())
staff=list(map(int, input (). split (maxsplit=amount_staff)))
amount_zakazov=int(input())
zakazi=list(map(int, input (). split (maxsplit=amount_zakazov)))
for i in range (amount_staff):
    if staff[i]<zakazi.count(i+1):
        print ("yes")
    else:
        print ("no")


