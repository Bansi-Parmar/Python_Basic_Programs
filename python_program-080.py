## 80.  A
##      A B
##      A B C
##      A B C D
##      A B C D E

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
for r in range(1,n+1):
       line = ''
       for c in range(1,r+1):
              line = line + ('{} '.format(chr(c+64)))
       print((line .ljust(n*2)))
