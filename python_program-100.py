## 100. Write a program to generate and display Floyd’s triangle as shown below:
##     1
##     2 3
##     4 5 6
##     7 8 9 10
##     11 12 13 14 15

print('\n\t pyramid')
print('\t..........\n')

n = int(input('Enter No :- '))
t=1
for r in range(1,n+1):
       for c in range(1,r+1):
              print(t,end=' ')
              t+=1
       print()




       
