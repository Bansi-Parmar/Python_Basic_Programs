## 112. To find out the total number of an even digits within the given number
##      and print the sum of all even digits.


print('\n\t Even Digit Count')
print('\t........\n')

n = int(input("Enter MAX Number :- "))
c=0
print('\nAll EVEN numbers within the {}  are :- '.format(n))
for i in range(1,n+1):
       if(i%2 == 0):
              c+=1
              print(i,end=' ')
print('\n\nTotal EVEN numbers within the {}  are :- '.format(n),c)
