def get_hash(s, x, p):
    hs = 0
    for i in range(len(s)):
        hs = (hs*x+ord(s[i])) % p
    return hs
    
def fun(s, g, x, p):
    k = 1
    if s!=g:
        g = g[1:]+g[0]
        hs = get_hash(s,x,p)
        hg = get_hash(g,x,p)
        xg = 1
        for i in range(len(s)-1):
            xg = (xg*x)%p
        for i in range(len(s)-1):
            if hs == hg:
                break
            else:
                hg = (x*(hg-ord(g[i])*xg)+ord(g[i]))%p
                k+=1
        if hs == hg:
            print(k)
        else:
            print(-1)
    else:
        print(0)
        
def main():
    s = input()
    g = input()
    x = 26
    p = 1e9 + 7
    fun(s,g,x,p)
    
main()