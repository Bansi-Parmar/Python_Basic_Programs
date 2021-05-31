## 79.  E D C B A
##        D C B A
##          C B A
##            B A
##              A

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
for r in range(n,0,-1):
       line = ''
       for c in range(r,0,-1):
              line = line + ('{} '.format(chr(c+64)))
       print((line .rjust(n*2)))
