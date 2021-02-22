#5 из 10.02
def NOK(a,b):
    k=a*b
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
         b = b % a
    m=a+b
    print("НОК=",k/m)
    
    
NOK(int(input()),int(input()))