##     111. To find out the total number of an odd digits within the given number
##          and print the sum of all odd digits.


print('\n\t ODD Digits Count')
print('\t..................\n')

n = int(input("Enter max Number :- "))
c=0
print('\nAll ODD numbers within the {}  are :- '.format(n))
for i in range(1,n+1):
       if(i%2 != 0):
              c+=1
              print(i,end=' ')
print()
print('\nTotal ODD numbers within the {}  are :- '.format(n),c)
