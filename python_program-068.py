## 68.         1
##           1   2
##         1   2   3
##       1   2   3   4

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(1,n+1):
       line = ''
       for c in range(1,r+1):
              line = line + ('{} '.format(c))
       print((line .center(n*2)))
