def prefix(s,l):
    pref = [0] * l
    for i in range(l - 1):
        j=pref[i]
        while j>0 and s[i+1] != s[j]:
            j = pref[j-1]
        if (s[i+1] == s[j]):
            pref[i+1] = j + 1
        else:
            pref[i+1] = 0
    return pref
def main():
    s = input()
    l=len(s)
    pref = prefix(s,l)
    if (l%(l-pref[-1])==0):
        print(l//(l-pref[-1]))
    else:
        print("1")
main()