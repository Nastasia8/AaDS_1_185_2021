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
'''
1-4 строчки ввод данных
5-6 заказ от количества товаров-1 уменьшается на 1
7-11 если количество товаров не = 0 то выводы
'''