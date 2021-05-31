## 64.   1
##       1 4
##       1 4 9
##       1 4 9 16 
##       1 4 9 16 25

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(1,n+1):
       line = ''
       i=1
       for c in range(r):
              line = line + ('{} '.format(i*i))
              i=i+1
       print((line .ljust(n*2)))
      
       
       
