def getHesh(string, n, p, x):
    res = 0
    for i in range(n):
        res = (res * x + ord(string[i])) % p
    return res

def RobinKarpAlgorithm(string, T, p, x):
    ht = getHesh(T, len(T), p, x)
    hs = getHesh(string, len(string), p, x)
    xt = 1
    for i in range(len(T)):
        xt = (xt * x) % p
    for i in range(len(string)):
        if (ht == hs):
            return i
        ht = (ht * x - ord(T[i]) * xt + ord(T[i])) % p
    return -1

def main():
    p = 1e9 + 7
    x = 26
    S = str(input())
    T = str(input())
    print(RobinKarpAlgorithm(S, T, p, x))

main()