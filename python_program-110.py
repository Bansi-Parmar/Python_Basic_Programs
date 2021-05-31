## 110. Write a program to evaluate the function
##      y=x^n
##      where n is a non-negative integer.


print('\n\t y=x^n')
print('\t........\n')

x = int(input("Enter base value x :- "))
n = int(input("Enter upper value of x :- "))
if(n < 0):
       print('NOT a Valid Number Format')
else:
       print('y={}^{} :- '.format(x,n),x**n)
