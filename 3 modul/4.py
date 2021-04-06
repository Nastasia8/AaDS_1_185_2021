def prefix(s):
    g = [0] * len(s)
    for i in range(len(s)-1):
        j = g[i]
        while j > 0 and s[j] != s[i + 1]:
            j = g[j - 1]
        if s[j] == s[i + 1]:
            g[i+1] = j + 1
        else:
            g[i+1] = 0
    return g


def main():
    s = input()
    pref=prefix(s)
    print (len(s)-pref[-1])


main()