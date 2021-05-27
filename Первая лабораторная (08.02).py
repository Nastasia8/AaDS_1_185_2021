#2.1
print("№2 (Sposob 1)")
a=list(range(1,21,2))
b=list()
for i in a:
    b.append(i**2)
print(a)
print(b)

#2.2
print("№2 (Sposob 2)")
print([number**2 for number in range (1,21,2)])

#3
print("№3")
k = int(input("Vvedite chislo k = "))
n = 1
f = 1
for n in range (n, k+1):
    f*=(2**n)-1
print(f)

#4.1
print("№4 (Sposob 1)")
summa = 0
a = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
for i in a:
    if i < 0:
        summa += 1
print(summa)

#4.2
print("№4 (Sposob 2)")
summa = 0
a = [7, 1, 3, 4, 3, 9, 14, -5, -17, -13, -19, -18]
i = -1
while a[i] < 0:
    summa += a[i]
    i -= 1
print (summa)

#5
print("№5")
def step(y,z):
    a = list()
    for i in range (1,21):
        if (i%2) != 0:
            a.append(i**y**z)
y=int(input("Vvedite chislo y = "))
z=int(input("Vvedite chislo z = "))
print(step(y,z))

#6
print("№6")
words = "Hello hi how hello are and you I am fine thank you and you hello You Thank And"
dict = {}
for word in words.split(" "):
    if word in dict:
        dict[word] = dict[word]+1
    else:
        dict[word] = 1
print(dict)

#9
print("№9") #В ответе ещё пишется none, понятия не имею почему
def TrueFalse (R, spisok):
    if R == spisok:
        print("True")
    else:
        print("False")
        
R = [1, 2, 3, 4]
spisok = [1, 2, 4, 5]
print(TrueFalse(R, spisok))

#10
print("№10")
spisok = [6, 43, -2, 11, -55, -12, 3, 345, 0]
spisok_key = {keys: "positive" if keys>0 else "negative" if keys<0 else "zero" for keys in spisok}
print(spisok_key)