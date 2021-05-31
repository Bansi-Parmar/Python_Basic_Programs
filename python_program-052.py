## 52.   1 2 3 4 5
##       2 3 4 5
##       3 4 5
##       4 5
##       5

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
i=1
for r in range(n,0,-1):
       line = ''
       for c in range(i,r+i):
              line = line + ('{} '.format(c))
       i=i+1
       print((line .ljust(n*2)))
       
