## 82.  E D C B A
##      E D C B
##      E D C
##      E D
##      E

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(n,0,-1):
       line = ''
       i = n
       for c in range(r,0,-1):
              line = line + ('{} '.format(chr(i+64)))
              i=i-1
       print((line .ljust(n*2)))
