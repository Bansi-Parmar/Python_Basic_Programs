## 15. SUM = 12 + 22 + 32 + 42 + 52 + 62 + 72 + ... and so on

print('\n\t Calculation(1+4+9...) of First given No')
print('\t..........................................\n')

no = int(input("Enter number :- "))
s = 0
for i in range(1,no+1):
       s = s + (i**2)
print("Calculation (1+4+9....) of First {} Number is :- ".format(no),s)
