## 20. SUM = 1 + 8 + 27 + 64 + … and so on

print('\n\t Calculation(1 + 8 + 27...) of First given No')
print('\t................................................\n')

no = int(input("Enter number :- "))
s = 0
for i in range(1,no+1):
       s = s + (i**3)
       
print("Calculation (1 + 8 + 27...) of First {} Number is :- ".format(no),s)


