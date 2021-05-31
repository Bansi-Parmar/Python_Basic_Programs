## 85.          E
##            D E
##          C D E
##        B C D E
##      A B C D E

print('\n\t patterns')
print('\t...........\n')


n = int(input("Enter No of Rows :- "))

for r in range(1,n+1):
       line = ''
       i=n-(r -1)
       for c in range(r):
              line = line + ('{} '.format(chr(i+64)))
              i=i+1
       print((line .rjust(n*2)))
