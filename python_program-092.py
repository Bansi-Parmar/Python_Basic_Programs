## 92. find out N!.

print('\n\t find out N!')
print('\t..............\n')

n = int(input("Enter N :- "))
fact=1
if(n == 0):
       print('{}! = 1'.format(n))
else:
       for no in range(1,n+1):
              fact = fact * no
       print('{}! = '.format(n),fact)

       
