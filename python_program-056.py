## 56.   5 5 5 5 5
##       4 4 4 4
##       3 3 3
##       2 2
##       1

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(n,0,-1):
       print((('{} '.format(r)*r) .ljust(n*2)))
      
       
       
