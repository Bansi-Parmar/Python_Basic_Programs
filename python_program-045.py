## 45.           1 
##             2 1 
##           3 2 1 
##         4 3 2 1
##       5 4 3 2 1
print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
i=1
for r in range(1,n+1):
       line = ''
       for c in range(r,0,-1):
              line = line + ('{} '.format(c))
       print((line .rjust(n*2)))
       
