## 107. To find the value of the following formula:
##      nCr = n!/(r! * (n-r)! )


print('\n\t nCr = n!/(r! * (n-r)!)')
print('\t........................\n')

n = int(input("Enter N :- "))
r = int(input("Enter R :- "))
 
def nCr(n, r): 
    return (fact(n) / (fact(r)  
                * fact(n - r))) 
  
def fact(n): 
    f = 1
    for i in range(2, n+1): 
        f = f * i  
    return f 

print('{}C{} is :- '.format(n,r),int(nCr(n, r))) 


       
