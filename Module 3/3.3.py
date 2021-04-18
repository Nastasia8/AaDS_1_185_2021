string = input()
for i in range(1, (len(string) // 2 + 1)):
    if string[:i] * (len(string) // i) == string:
        print (len(string) // i)
        break
else:
    print (1)
#Там TL, блин, но код работает
#Я ещё молодой у меня времени много, посему исправлять не стал, пока что