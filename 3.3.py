def len_max(a):
    x = len(a)
    for j in range(1, x):
        for i in range(x-1):
            if len(a[i]) < len(a[i+1]):
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
    max_a = len(a[0])
    return max_a

def fun(a,s):
    for i in range(len(a)):
        if len(a[i]) < len_max(a):
            for j in range(len(a[i]), len_max(a)):
                a[i] += s
    return(a)




a = ["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]
b = ["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
c = ["tiger",  "leopard", "elephant", "camel", "fox", "wolf", "raccoon"]

s = input("Знак: ")
print(fun(a, s))
print(fun(b, s))
print(fun(c, s))
