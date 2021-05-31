## 63.           1
##             2 2
##           3 3 3
##         4 4 4 4
##       5 5 5 5 5

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
i=0
for r in range(1,n+1):
       print((('{} '.format(r)*r) .rjust(n*2)))
       i=i+1
      
       
       
