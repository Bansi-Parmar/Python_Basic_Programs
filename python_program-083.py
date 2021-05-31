## 83.  A B C D E
##        B C D E
##          C D E
##            D E
##              E

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
i=1
for r in range(n,0,-1):
       line = ''
       for c in range(i,r+i):
              line = line + ('{} '.format(chr(c+64)))
       i=i+1
       print((line .rjust(n*2)))
