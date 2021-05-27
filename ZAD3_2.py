n = int(input("n = "))
s = input("Символ = ")
for i in range(1,n+1):
    print(s*i)
print()
for i in range(n,0, -1):
    print(s*i)
print()
for i in range(n):
    print(" "*i + s*(n-i))
print()
for i in range(n-1, -1, -1):
    print(" "*i + s*(n-i))
print("------------------------------")
i = 0
while i <= n:
    print(s*i)
    i += 1
print()
i = n
while i > 0:
    print(s*i)
    i -= 1
print()
i = 0
while i <= n:
    print(" "*i + s*(n-i))
    i += 1
print()
i = n-1
while i > -1:
    print(" "*i + s*(n-i))
    i -= 1