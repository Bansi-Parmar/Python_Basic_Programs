## 38. 1 
##     1 2 
##     1 2 3 
##     1 2 3 4 
##     1 2 3 4 5 

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(1,n+1):
       for c in range(1,r+1):
              print(c,end=' ')
       print()

