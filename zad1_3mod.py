def z_funs(s):
    a=[0]*len(s)
    l=r=0
    for i in range(1,len(s)):
        if i<=r:
            a[i]=min(a[i-l],r-i+1)
        while a[i]+i<len(s) and s[a[i]]==s[a[i]+i]:
            a[i]+=1
        if a[i]+i-1>r:
            l=i
            r=a[i]+i-1
    return a
def main():
    s=input()
    t=input()
    z=z_funs(t+"#"+s)
    for i in range(len(z)):
        if len(t)==z[i]:
            print(i-len(t)-1, end=" ")


main()