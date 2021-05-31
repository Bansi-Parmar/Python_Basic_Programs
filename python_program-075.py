## 75.  A A A A A
##        B B B B
##          C C C
##            D D
##              E

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
i=1
for r in range(n,0,-1):
       line = ''
       for c in range(1,r+1):
              line = line + ('{} '.format(chr(i+64)))
       print((line .rjust(n*2)))
       i=i+1
