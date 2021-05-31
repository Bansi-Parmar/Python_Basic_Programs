## 19. SUM = 1 + 1/4 + 1/9 + 1/16 + 1/25 + … and so on

print('\n\t Calculation(1 + 1/4 + 1/9...) of First given No')
print('\t................................................\n')

no = int(input("Enter number :- "))
s = 0
for i in range(1,no+1):
       s = s + (1/(i**2))
       
print("Calculation (1+2+4+8...) of First {} Number is :- ".format(no),s)


