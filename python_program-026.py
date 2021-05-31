## 26. To calculate the average of first N odd numbers.

print('\n\t average of first N odd numbers')
print('\t.................................\n')

no = int(input("Enter Number :- "))
s = 0
##for i in range(2,no+no,2):
##       s = s +(2*i+1)
##       print(s)

for i in range(1,no*2,2):
       s +=i      
print("average of first {} odd numbers is :- ".format(no),s/no)


