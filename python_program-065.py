## 65.             1
##               4 1
##             9 4 1
##          16 9 4 1
##       25 16 9 4 1

print('\n\t patterns')
print('\t...........\n')

n = int(input("Enter No of Rows :- "))
i=1
for r in range(1,n+1):
       line = ''
       for c in range(r,0,-1):
              line = line + (' {}'.format(c*c))
       if(r > 4):
              print((line .rjust((n*3))))
       else:
              print((line .rjust((n*3))))
