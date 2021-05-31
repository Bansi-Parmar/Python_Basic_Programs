## 14. SUM = 1 + 4 – 9 + 16 – 25 + 36 - … and so on

print('\n\t Calculation(1+4-9...) of First given No')
print('\t..........................................\n')

no = int(input("select a number :- "))
s = 1
for i in range(2,no+1):
       if(i % 2 == 0):
              s = s + (i**2)
       else:
              s = s - (i**2)
              
print("Calculation (1+4-9...) of First {} Number is :- ".format(no),s)
              

                                        
                                     

