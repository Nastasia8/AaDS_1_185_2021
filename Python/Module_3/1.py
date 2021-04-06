# from math import abs


def get_hash(s, n, p, x):
    res = 0
    for i in range(n):
        res = (res*x+ord(s[i])) % p
    return res


def rabin_karp(s, t, p, x):
    arr = []
    # Вычислим хэш искомой строки
    ht = get_hash(t, len(t), p, x)
    # Вычислим хэш строки S
    hs = get_hash(s, len(t), p, x)
    # Вычилсим xt (для скользящего хэша)
    xt = 1
    for i in range(len(t)):
        xt = (xt*x) % p

    for i in range(len(s)-len(t)+1):
        if ht == hs:
            # Можно добавить проверку на коллизию
            arr.append(i)
        if i+len(t) < len(s):
            hs = (hs * x - ord(s[i]) * xt + ord(s[i + len(t)]))
            hs = (hs + p) % p
    for i in range(len(arr)):
        print(arr[i], end=' ')

    return -1


def main():
    p = 1e9 + 7
    x = 26
    s = str(input())
    t = str(input())
    rabin_karp(s, t, p, x)


main()
