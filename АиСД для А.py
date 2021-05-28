#2.7
n=int(input())
print("Initial array:")
Massive=[]
[Massive.append(input()) for _ in range (n)]

for i in range(len(Massive)-1):
    print(Massive[i], end=", ")
print(Massive[len(Massive)-1])
faza = 0
m = len(Massive[0])
for i in range(m-1,-1,-1):
    print("**********")
    faza += 1
    print("Phase",faza)
    bucket = [[] for _ in range(10)]
    for j in range(len(Massive)):
        bucket[ord(Massive[j][i]) - ord("0")].append(Massive[j])
    for j in range(10):
        if len(bucket[j])==0:
            print("Bucket ",str(j),": empty",sep="")
        else:
            print("Bucket ",str(j),": ",sep="", end="")
            for k in range(len(bucket[j])-1):
                print(bucket[j][k],end=", ")
            print(bucket[j][len(bucket[j])-1])
    p = 0
    for j in range(10):
        for k in range(len(bucket[j])):
            Massive[p] = bucket[j][k]
            p += 1
print("**********")
print("Sorted array:")
for i in range(len(Massive)-1):
    print(Massive[i], end=", ")
print(Massive[len(Massive)-1])
#3.3
def prefix(A, n):
    res = [0]*n
    res[0] = 0
    for i in range(n-1):
        j = res[i]
        while (j > 0 and A[i+1] != A[j]):
            j = res[j-1]
        if (A[i+1] == A[j]):
            res[i+1] = j + 1
        else:
            res[i+1] = 0
    return res

A = input()
res = prefix(A, len(A))
k = len(A) - res[len(A)-1]
if (len(A) % k == 0):
    print(len(A)//k)
else:
    print(1)
#3.4
def prefix_func(k, n):
    s_res = [0]*n
    s_res[0] = 0
    for i in range(n-1):
        j = s_res[i]
        while (j > 0 and k[i+1] != k[j]):
            j = s_res[j-1]
        if (k[i+1] == k[j]):
            s_res[i+1] = j + 1
        else:
            s_res[i+1] = 0
    return s_res

S = input()
k = prefix_func(S, len(S))
print(len(S) - k[len(k)-1])
#4.1
s = input()
k = 0
stack = []
for i in s:
    if i==")":
        if stack:
            stack.pop()
            k+=2
    else:
        stack.append(i)
print(len(s) - k)
#4.2
n = int(input())
string = list(map(int, input().split()))
stack = []
isPsk = True
num = 1
for i in string:
    for j in range(len(stack)):
        if stack and num == stack[-1]:
            stack.pop()
            num += 1
    if i != num:
        if stack and i > stack[-1]:
            isPsk = False
            break
        stack.append(i)
    else:
        num += 1
if isPsk:
    print ("YES")
else:
    print ("NO")
#4.3
n = int(input())
nums = list(map(int,input().split()))[:n]
d = {i:nums[i] for i in range (n)}
stack = []
index = [0]*n
for i in range(n-1,-1,-1):
    while stack and stack[-1][1] >= d[i]:
        stack.pop()
    if not stack:
        index[i] = -1
    else:
        index[i] = stack[-1][0]
    stack.append([i, d[i]])
print(*index)    
#4.4
n, k = map(int, input().split())
nums = list(map(int, input().split()))
stack = []
res = [0] * n
for i in range(n):
    while stack and nums[i] < nums[stack[-1]]:
        res[stack.pop()] = i
    stack.append(i)
while stack:
    res[stack.pop()] = n
i_n = 0
for i in range(n - k + 1):
    if i_n < i:
        i_n = i
    while res[i_n] < i + k:
        i_n = res[i_n]
    print(nums[i_n])
#5.1
class Node:
    __size = 0 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
        Node.__size+=1 
        
    def add(self, value):
        if value == self.data:
            return
        if value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)
                
    def find_forks(self): 
        if self.left:
            self.left.find_forks()
        if self.left or self.right:
            if self.left and not self.right:
                print(self.data, end =" ")
            elif not self.left and self.right:
                print(self.data, end =" ")
        if self.right:
            self.right.find_forks()
    def find_fork(self):
        if self.left:
            self.left.find_fork()
        if (self.left and self.right is None) or (self.left is None and self.right):
            print(self.data)
        if self.right:
            self.right.find_fork()
def build_tree(elements): 
    r = Node(elements[0])
    for item in range(1, len(elements)):
        r.add(elements[item])
    return r

def main(): 
    n =list(map(int, input().split(" "))) 
    n.pop()

    tree = build_tree(n)

    tree.find_fork()
 
main()
#5.2
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add(self, value):
        if value == self.data:
            return
        if value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)
                
def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right)) + 1

def build_tree(elements):
    root = Node(elements[0])
    for item in range(1, len(elements)):
        root.add(elements[item])
    return root

def check_balance(tree):
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and check_balance(tree.right) and check_balance(tree.left)):
        return True
    return False
    
def main():
    n =list(map(int, input().split(" "))) 
    n.pop()

    tree = build_tree(n)

    if check_balance(tree):
        print("YES")
    else:
        print("NO")
 
main()
#5.3
from math import gcd
def build(v,l,r,do,a):
    if r - l == 1:
        do[v]= a[l]
        return
    m=(r+l)//2
    build(2*v+1,l,m,do,a)
    build(2*v+2,m,r,do,a)
    do[v] = gcd(do[2*v+1],do[2*v+2])

def nod(v,l,r,do,ql,qr):
    if ql<=l and qr>=r:
        return do[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    tl = nod (2*v+1,l,m,do,ql,qr)
    tr = nod (2*v+2,m,r,do,ql,qr)

    return gcd(tl,tr)

def main():
    n=int(input())
    a= list(map(int, input().split(maxsplit=n)))
    do= [0]*4*n
    build(0,0,n,do,a)
    q = int(input())
    index = []
    while q !=0:
        l,r = map(int,input().split())
        index.append(nod(0,0,n,do,l-1,r))
        q-=1
    print(*index)


main()
#5.5
from math import gcd
def build(v,l,r,do,a):
    if r - l == 1:
        do[v]= a[l]
        return
    m=(r+l)//2
    build(2*v+1,l,m,do,a)
    build(2*v+2,m,r,do,a)
    do[v] = gcd(do[2*v+1],do[2*v+2])

def update(v,l,r,do,idx,value):
    if r-l==1:
        do[v]=value
        return
    m=(r+l)//2
    if idx < m:
        update (2*v+1,l,m,do,idx,value)
    else:
        update (2*v+2,m,r,do,idx,value)
    do[v]= gcd (do[2*v+1],do[2*v+2])
def nod(v,l,r,do,ql,qr):
    if ql<=l and qr>=r:
        return do[v]
    if ql >= r or qr<=l:
        return 0
    m = (r+l)//2
    tl = nod (2*v+1,l,m,do,ql,qr)
    tr = nod (2*v+2,m,r,do,ql,qr)
    return gcd(tl,tr)

def main():
    n=int(input())
    a= list(map(int, input().split(maxsplit=n)))
    do= [0]*4*n
    build(0,0,n,do,a)
    q = int(input())
    index = []
    while q !=0:
        que,l,r = map(str,input().split())
        if que=="s":
            index.append(nod(0,0,n,do,int(l)-1,int(r)))
        else:
            update(0,0,n,do,int(l)-1,int(r))
        q-=1
    print(*index)


main()