## 7. To check whether the given number is of one digited or two digited or
##    three digited or more digited.

print('\n\t Total Digit Of Number')
print('\t.........................\n')

n = int(input("Enter Number :- "))
no = len(str(n))

print("{} is {} digited".format(n,no)if(no <= 3)else "{} is more digited.".format(n))       
