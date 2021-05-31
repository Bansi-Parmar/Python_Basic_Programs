## 18. SUM = 1 + 2 + 4 + 8 + 16 + 32 + 64 + … and so on

print('\n\t Calculation(1+2+4+8...) of First given No')
print('\t................................................\n')

no = int(input("Enter number :- "))
s = 1
t = 1
for i in range(2,no+1):
       t = t*2
       s = s + t
       
print("Calculation (1+2+4+8...) of First {} Number is :- ".format(no),s)


