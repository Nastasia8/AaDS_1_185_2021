

def pre_count(string):
    p = [0]*len(string)
    for i in range(len(string)-1):
        j = p[i]
        while j > 0 and string[j] != string[i+1]:
            j = p[j-1]
        if string[j] == string[i+1]:
            p[i+1] = j+1
        else:
            p[i+1] = 0
    return p

string = input()
pre = pre_count(string)
index = []
if 1 in pre:
    for i in range(len(string)):
        if pre[i] == 1:
            index.append(i)
    pattern = string[:index[-1]]
else:
    pattern = string
if string==pattern*(len(string)//len(pattern)):
    print(len(string) // len(pattern))
else:
    print(1)