s=5
def funk3(s):
  for i in range(s):
    for j in range(s):
      if i+j<s:
        print("0 ",end="")
    print("")
  print(" ")
  for i in range(s):
    for j in range(s):
      if i>=j:
        print("0 ",end="")
    print("")
  print("")
  i=0
  j=0
  while i<=s:
    while j<=s:
      #print(i,j)
      if i+j>s:
        print("0 ",end="")
      else:
        print("  ",end="")
      j+=1
    j=0
    i+=1
    print("")
  print("")
  i=0
  j=0
  while i<=s:
    while j<=s:
      #print(i,j)
      if j>i:
        print("0 ",end="")
      else:
        print("  ",end="")
      j+=1
    j=0
    i+=1
    print("")
  print("")
funk3(s)