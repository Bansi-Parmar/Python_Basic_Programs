## 89.   * * * * *
##       *       *
##       *       *
##       *       *
##       * * * * *

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(n):
       for c in range(n):
              if(r==0 or r==n-1 or c==0 or c==n-1):
                     print('*',end=' ')
              else:
                     print(' ',end=' ')
       print()
             
