## 70.         a
##           a   b
##         a   b   c
##       a   b   c   d

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(1,n+1):
       line = ''
       for c in range(1,r+1):
              line = line + ('{} '.format(chr(c+96)))
       print((line .center(n*2)))
