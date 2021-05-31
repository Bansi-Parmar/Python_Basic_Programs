## 87.         Z
##           Z   Y
##         Z   Y   X
##       Z   Y   X   W
##     Z   Y   X   W   V

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
for r in range(1,n+1):
       line = ''
       i = 90
       for c in range(1,r+1):
              line = line + ('{} '.format(chr(i)))
              i = i-1
       print((line .center(n*2)))
