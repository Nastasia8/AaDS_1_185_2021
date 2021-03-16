

def get_hash(string, n, x, p):
    result = 0
    for i in range(n):
        result = ((result*x) + ord(string[i])) % p
    return result 

def rabin_karp(text, pattern, x, p):
    result = []
    cur_hash = get_hash(text, len(pattern), x ,p)
    req_hash = get_hash(pattern, len(pattern), x, p)
    xt = 1
    for i in range(len(pattern)):
        xt = (xt*x) % p

    for i in range(len(text)-len(pattern)+1):
        if req_hash == cur_hash:
            result.append(i)
        if i+len(pattern) < len(text):
            cur_hash = cur_hash*x - ord(text[i])*xt + ord(text[i+len(pattern)])
            cur_hash = (cur_hash+p) % p
            
    return result

text = input()
pattern = input()
p = 1e9 + 7
x = 27
print(*rabin_karp(text, pattern, x, p))