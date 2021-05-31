## 8. To check whether the given number is divisible by 7 or not.

print('\n\t Number is divisible by 7 or not')
print('\t.................................\n')

n = int(input("Enter Number :- "))
print("{} is divisible by 7".format(n) if(n % 7 == 0) else "{} is NOT divisible by 7".format(n))  
