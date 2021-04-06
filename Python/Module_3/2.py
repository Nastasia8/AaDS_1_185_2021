# from math import abs


def get_hash(s, n, p, x):
    res = 0
    for i in range(n):
        res = (res*x+ord(s[i])) % p
    return res


def rabin_karp(s, t, p, x):
    arr = []
    k = 0
    # Вычислим хэш искомой строки
    ht = get_hash(t, len(t), p, x)
    # Вычислим хэш строки S
    hs = get_hash(s, len(t), p, x)
    # Вычилсим xt (для скользящего хэша)
    xt = 1
    for i in range(len(t)):
        xt = (xt*x) % p

    for i in range(len(t)):
        if ht == hs:
            # Можно добавить проверку на коллизию
            return k
        else:
            ht = (ht * x - ord(t[i]) * xt + ord(t[i]))
            ht = (ht + p) % p
            k += 1

    return -1


def main():
    p = 1e9 + 7
    x = 26
    s = str(input())
    t = str(input())
    print(rabin_karp(s, t, p, x))


main()
