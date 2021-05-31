## 101. Write a program to generate and display the following pattern:
##          1
##         0 1
##        1 0 1
##       0 1 0 1
##      1 0 1 0 1
##     0 1 0 1 0 1

print('\n\t pyramid')
print('\t..........\n')

n = int(input('Enter No :- '))
t=1
for r in range(1,n+1):
       line = ''
       for c in range(1,r+1):
              line = line + ('{} '.format(t%2))
              t+=1
       print((line .center(n*2)))
       if(r%2 == 0):
              t=1
       else:
              t=0



       
