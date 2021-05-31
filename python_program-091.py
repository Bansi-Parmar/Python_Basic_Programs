## 91.      0
##        -1 0 1
##      -2 -1 0 1 2
##    -3 -2 -1 0 1 2 3
##  -4 -3 -2 -1 0 1 2 3 4

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for i in range(0,n+1):
       for c in range(1,n-i+2):
              print(end='   ')
       for c in range(i,-1,-1):
              print('{}'.format(-c),end=' ')
       for c in range(1,i+1):
              print(c,end=' ')
       print()

       
