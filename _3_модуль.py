#3.1
#
#def z_fun(s):
#   arr=[0]*len(s)
#    l = r =0
#    for i in range(1, len(s)):
#        if i <= r:
#            arr[i] = min(arr[i-l], r-i+1)
#        while arr[i] + i < len(s) and s[arr[i]] == s[arr[i]+i]:
#            arr[i] += 1
#        if arr [i] + i - 1 > r:
#            l=i
#            r = arr[i] + i - 1
#    return arr    
#
#def main():
#    s = input()
#    t = input()
#    z = z_fun(t+"#" + s)
#    for i in range(len(z)):
#        if len(t) == z[i]:
#            print(i- len(t) - 1, end = "  ")
#    
#main()    
#
#3.2
#def get_hash(s, x, c):
#    ha = 0
#    for i in range(len(s)):
#        ha = (ha*x+ord(s[i])) % c
#    return ha
#    
#def fun(s, t, x, c):
#    k = 1
#    if s!=t:
#        t = t[1:]+t[0]
#        ha = get_hash(s,x,c)
#        ht = get_hash(t,x,c)
#        xt = 1
#        for i in range(len(s)-1):
#            xt = (xt*x)%p
#        for i in range(len(s)-1):
#            if hs == ht:
#                break
#            else:
#                ht = (x*(ht-ord(t[i])*xt)+ord(t[i]))%p
#                k+=1
#        if ha == ht:
#            print(k)
#        else:
#            print(-1)
#    else:
#        print(0)
#        
#def main():
#    s = input()
#    t = input()
#    x = 26
#    c = 1e9 + 7
#    fun(s,t,x,c)
#    
#main()
#
#3.3
#def prefix(s):
#    a = [0] * len(s)
#    ind = 0
#    for i in range(len(s)-1):
#        j = a[i]
#        while j > 0 and s[j] != s[i + 1]:
#            j = a[j - 1]
#        if s[j] == s[i + 1]:
#            a[i+1] = j + 1
#        else:
#            a[i+1] = 0
#        if a[i+1] < 2:
#            ind = i+1
#    return a, ind
#
#def result(s):
#    pref, ind = prefix(s)
#    if len(s) == 2 and s[0] == s[1]:
#        return 2
#    if 2 in pref:
#        t = s[:ind]
#    else:
#        return 1
#    k = 0
#    a, NULL = prefix((t+"$"+s))
#    for i in range(len(a)):
#        if a[i] == len(t):
#            k += 1
#    if k*t == s:
#        return k
#    return 1
#
#def main():
#    s = input()
#    print(result(s))
#
#main()
#3.4
#
#def prefix(a):
#    g = [0] * len(a)
#    ind = 1
#    for i in range(len(a)-1):
#        j = p[i]
#        while j > 0 and a[j] != a[i + 1]:
#            j = g[j - 1]
#        if a[j] == a[i + 1]:
#            g[i+1] = j + 1
#        else:
#            g[i+1] = 0
#        if g[i+1] < 2:
#            ind = i+1
#    return ind
#
#
#def main():
#    a = int(input())
#    print(prefix(a))
#
#main()