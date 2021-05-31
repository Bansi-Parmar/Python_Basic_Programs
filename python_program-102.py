## 102. Write a program to generate and display the following pattern:
##     1 *
##     1 * 2 * *
##     1 * 2 * * 3 * * *
##     1 * 2 * * 3 * * * 4 * * * *
##     1 * 2 * * 3 * * * 4 * * * * 5 * * * * *

print('\n\t pyramid')
print('\t..........\n')

n = int(input('Enter No :- '))

for r in range(1,n+1):
       for c in range(1,r+1):
              print('{}{}'.format(c,('*')*c),end='')
       print()


       
