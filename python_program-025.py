## 25. To calculate the sum of first N natural numbers.

print('\n\t sum of first N natural numbers')
print('\t.................................\n')

no = int(input("Enter Number :- "))

##def summ(l):
##       s=0
##       for i in range(1,l+1):
##              s = s + i
##       return s
##      

print("sum of first {} natural numbers is :- ".format(no),int(no * (no + 1) / 2))

