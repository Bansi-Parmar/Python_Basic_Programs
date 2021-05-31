## 72.   a   b   c   d
##         a   b   c
##           a   b
##             a

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(n,0,-1):
       line = ''
       for c in range(1,r+1):
              line = line + ('{} '.format(chr(c+96)))
       print((line .center(n*2)))
