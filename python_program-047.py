## 47.   1 2 3 4 5
##         1 2 3 4
##           1 2 3
##             1 2
##               1

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
i=1
for r in range(n,0,-1):
       line = ''
       for c in range(1,r+1):
              line = line + ('{} '.format(c))
       print((line .rjust(n*2)))
       
