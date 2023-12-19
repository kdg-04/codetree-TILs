n = int(input())  

satisfied = 0  
if n <= 0:    
    pass  

for i in range(2,n):  
    if n % i == 0:  
        satisfied = 1  

if satisfied == 1:
    print('C')
else:
    print('N')