A = [ [1, 2], [4, 5] ]
for i in range(len(A)):
    for j in range(len(A[i])):
      print(A[i][j], end = ' ')
    print()
for i in range(len(A)):
    for j in range(len(A[i])): 
      if i==j:
          A[i][j]=A[i][j]*2
      print(A[i][j], end = ' ')
    print() 