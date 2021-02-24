x=int(input("x = "))
y=int(input("x = "))
def f(a,b):
  h=x
  h1=y
  while a> 0 and b> 0:
    if a>b:
      a=a%b
    else:
      b=b%a
  print("НОД ("+str(h)+";"+ str(h1)+") = "+str(a+b))
f(x,y)