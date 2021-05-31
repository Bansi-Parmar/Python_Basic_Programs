## 48.   5 4 3 2 1
##       5 4 3 2
##       5 4 3
##       5 4
##       5

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(n,0,-1):
       i = n
       for c in range(r,0,-1):
              print(i,end=' ')
              i=i-1
       print()
       
