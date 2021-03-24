  

def pre_count(string):
    p = [0]*len(string)
    for i in range(len(string)-1):
        j = p[i]
        while j > 0 and string[j] != string[i+1]:
            j = p[j-1]
        if j == 1:
            print(p)
            return i
        if string[j] == string[i+1]:
            p[i+1] = j+1
        else:
            p[i+1] = 0
    print(p)
    return len(string)

def main():
    string = input()
    pre = pre_count(string)
    print(len(string), '/', pre, '=', len(string) // pre)
main()
