## 66.         1
##           2   2
##         3   3   3
##       4   4   4   4

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(1,n+1):
       print(('{} '.format((r))*r) .center(n*2))
       
