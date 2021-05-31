## 55.           5
##             5 4
##           5 4 3
##         5 4 3 2
##       5 4 3 2 1

print('\n\t patterns')
print('\t...........\n')
n = int(input("Enter No of Rows :- "))

for r in range(1,n+1):
       line = ''
       i=n
       for c in range(r):
              line = line + ('{} '.format(i))
              i=i-1
       print((line .rjust(n*2)))
       
       
