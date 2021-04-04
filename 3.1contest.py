s=input()
t=input()
spisok=[]
for i in range(len(s)-len(t)+1):
  if s[i:len(t)+i]==t:
    spisok.append(i)
print(*spisok)
