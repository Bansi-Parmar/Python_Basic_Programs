## 6. To check whether the given number is positive or negative or zero.

print('\n\t number is positive or negative or zero')
print('\t.........................................\n')

no = int(input("Enter Number :- "))

if(no > 0):
       print("{} is positive".format(no))
elif(no == 0):
       print("{} is zero".format(no))
else:
       print("{} is negative".format(no))
