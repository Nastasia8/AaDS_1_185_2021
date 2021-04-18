string = input()
for i in range(1, (len(string) // 2+1)):
    if string[:i] * (len(string) // i) == string:
        print (len(string) // i)
        break
else:
    print (1)