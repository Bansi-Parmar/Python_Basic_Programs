## 99. Generate the following “pyramid” of digits.
##            1
##          2 3 2
##        3 4 5 4 3
##      4 5 6 7 6 5 4
##    5 6 7 8 9 8 7 6 5
##  6 7 8 9 0 1 0 9 8 7 6
##7 8 9 0 1 2 3 2 1 0 9 8 7

print('\n\t pyramid')
print('\t..........\n')

n = int(input('Enter No :- '))

for i in range(1,n+1):
       t=i
       for c in range(1,n-i+2):
              print(end='  ')
       for c in range(i,0,-1):
              print(t,end=' ')
              t=t+1
              if t==10:
                     t=0
       t = t-2
       if t==-2:
              t=8
       for c in range(2,i+1):
              print(t,end=' ')
              t=t-1
              if t==-1:
                     t=9
       print()


       
