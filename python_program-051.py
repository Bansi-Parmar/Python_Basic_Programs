## 51.           5
##             4 5
##           3 4 5
##         2 3 4 5
##       1 2 3 4 5

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(1,n+1):
       line = ''
       i=n-(r -1)
       for c in range(r):
              line = line + ('{} '.format(i))
              i=i+1
       print((line .rjust(n*2)))
       
