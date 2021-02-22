#6 из 10.02
def getNodofPair(a,b):
    while a != 0 and b != 0:
        if a < b:
            a,b = b,a
        a%=b
    return b
    
def getNod(*params):
    d1=getNodofPair(params[0], params[1])
    if len(params)>2:
        i=2
        while i<len(params):
            d1=getNodofPair(params[i],d1)
            i+=d1
        return d1
    else:
        return d1


a=78
b=294
c=570
d=36
print("NOD ({0};{1};{2})={3}". format(a,b,c, getNod(a,b,c)))
print("NOD ({0};{1};{2};{3})={4}". format(a,b,c,d, getNod(a,b,c,d)))    
print("NOD ({0};{1})={2}". format(a,b, getNod(a,b)))   
    
def prime_factors(n):
    factors=[]
    delit=2
    while n>1:
        while n % delit ==0:
            factors.append(delit)
            n/=delit
        delit +=1
    return factors
    
def getNodPrimeFactors(*params):
    l=[]
    p=d1
    for n in params:
        l.append(set(prime_factors(n)))
    for m in set.intersection(*l):
        p*=m
    return p