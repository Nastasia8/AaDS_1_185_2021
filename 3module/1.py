
def get_hesh (s,n,p,x):
    res=0
    for i in range (n):
        res=(res*x+ord(s[i]))%p
    return res

def robin_karp (s,search,p,x):  
    ht=get_hesh(search,len(search),p,x)
    hs=get_hesh(s,len(search),p,x)
    xt=1
    for i in range (len(search)):
        xt=(xt*x)%p
    for i in range (len(s)-len(search)+1):
        if (ht==hs):
            print(i,end=" ")
        if (i +len(search)< len(s)):\
            hs=(hs*x-ord(s[i])*xt+ord(s[i+len(search)]))%p
            
def main ():
    string =input()
    search = input()
    p=1e9 + 7
    x=26
    robin_karp(string,search,p,x)

main()