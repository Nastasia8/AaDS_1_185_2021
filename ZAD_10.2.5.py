def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)
a=18
b=48
d=nok(a,b)
print("НОК ("+str(a)+";"+str(b)+") = "+str(d))