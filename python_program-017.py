## 17. SUM = x + x2 + x3+ x4 + x5 + x6… and so on

print('\n\t Calculation(x + x2 + x3...) of First given No')
print('\t................................................\n')

x = int(input("Enter X :- "))
no = int(input("Enter number :- "))
s = 0
for i in range(1,no+1):
##       s = s + pow(x, i)
       s = s + (x**i)       
print("Calculation (x + x2 + x3...) of First {} Number is :- ".format(no),s)


