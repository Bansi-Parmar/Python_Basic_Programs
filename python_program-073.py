## 73.   *   *   *   *
##         *   *   *
##           *   *
##             *

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))

for r in range(n,0,-1):
       print(('* '*r) .center(n*2))
