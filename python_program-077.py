## 77.          E
##            D D
##          C C C
##        B B B B
##      A A A A A

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
i=n
for r in range(1,n+1):
       line = ''
       for c in range(1,r+1):
              line = line + ('{} '.format(chr(i+64)))
       print((line .rjust(n*2)))
       i=i-1
