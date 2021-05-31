## 67.         4
##           3   3
##         2   2   2
##       1   1   1   1

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
i=0
for r in range(1,n+1):
       print(('{} '.format((n-i))*r) .center(n*2))
       i = i+1
