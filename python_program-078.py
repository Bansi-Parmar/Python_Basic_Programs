## 78.  A B C D E
##      A B C D
##      A B C
##      A B
##      A

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
for r in range(n,0,-1):
       line = ''
       for c in range(1,r+1):
              line = line + ('{} '.format(chr(c+64)))
       print((line .ljust(n*2)))
