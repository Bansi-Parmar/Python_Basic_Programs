## 16. SUM = x – x3/3! + x5/5! - x7/7! + x9/9! -… and so on

print('\n\t Calculation(x-x3/3!+x5/5!...) of First given No')
print('\t..................................................\n')

x = int(input("Enter X :- "))
no = int(input("Enter number :- "))
s = 0
c = 1
for i in range(1,no+1,2):
       fact=1
       for k in range(1,i+1):
              fact = fact * k
       if(c % 2 == 1):
              s = s + ((x**i)/(fact))
       else:
              s = s - ((x**i)/(fact))
       c = c + 1
print("Calculation (x-x3/3!+x5/5!...) of First {} Number is :- ".format(no),s)


