## 108. To find the value of the following formula:
##      nPr = n!/(n-r)!


print('\n\t nPr = n!/(n-r)!')
print('\t........................\n')

n = int(input("Enter N :- "))
r = int(input("Enter R :- "))
 
def nPr(n, r): 
    return (fact(n)/fact(n - r))
  
def fact(n): 
    f = 1
    for i in range(2, n+1): 
        f = f * i  
    return f 

print('{}P{} is :- '.format(n,r),int(nPr(n, r))) 


       
