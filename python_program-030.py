## 30. To check whether a given number N1 is divisible by the number N2 or not.

print('\n\t N1 is divisible by the number N2 or not')
print('\t..........................................\n')

n1 = int(input("Enter N1:- "))
n2 = int(input("Enter N2:- "))

print("{} is divisible by the number {}".format(n1,n2) if(n1 % n2 == 0) else "{} is NOT divisible by the number {}".format(n1,n2))

