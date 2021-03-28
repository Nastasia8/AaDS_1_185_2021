n = int(input())                                                
c = list(map(int,input().split()))                                       
a = int(input())                                                
k = list(map(int,input().split()))                                       
for i in range(0, a):                                        
    c[(k[i]) - 1] = c[(k[i])-1] - 1         
for i in c:                                                  
    if i <0:                                           
        print('yes')                                            
    else:                                                       
        print('no')  