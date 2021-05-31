## 34. To find sum of all odd digits and even digits from a given positive
##     number.

print('\n\t sum of all odd digits and even digits from a given positive number')
print('\t.....................................................................\n')

nos = int(input("Enter Number :- "))
no = nos
odd=0
even=0
for n in range(len(str(no))):
       if((int(no%10) % 2)== 0):
              even = even + int(no % 10)
       else:
              odd = odd + int(no % 10)
       no = no / 10

print("Sum of all ODD Digit in the {} :- ".format(nos),int(odd))
print("Sum of all EVEN Digit in the {} :- ".format(nos),int(even))

