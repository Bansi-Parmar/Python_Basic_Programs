## 84.  E
##      E D
##      E D C
##      E D C B
##      E D C B A

print('\n\t patterns')
print('\t...........\n')


n = int(input("Enter No of Rows :- "))

for r in range(1,n+1):
       line = ''
       i=n
       for c in range(r):
              line = line + ('{} '.format(chr(i+64)))
              i=i-1
       print((line .ljust(n*2)))
