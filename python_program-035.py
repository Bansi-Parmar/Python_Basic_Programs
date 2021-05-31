## 35. To find sum of all prime digits from a given number.

print('\n\t sum of all prime digits from a given number.')
print('\t...............................................\n')

n = int(input("Enter number :- "))
tno = n
psum = npsum = 0

while(tno > 0):
       dig = tno % 10
       tno = tno//10
       if((dig==1) or (dig==2) or (dig==3) or (dig==5) or (dig==7) or (dig==9)):
              psum = psum + dig

print("sum of {} prime number is : ".format(n),psum)


