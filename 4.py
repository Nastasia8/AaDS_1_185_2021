#4 из 10.02
def NOD(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
         b = b % a
    print ("НОД =", a+b)


NOD(int(input()),int(input()))