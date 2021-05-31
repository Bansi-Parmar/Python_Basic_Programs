## 113. To convert the given decimal number into its equivalent binary number.

print('\n\t Decimal to binary')
print('\t....................\n')

n = int(input("Enter Decimal Number :- "))

print('Binary Number {} is :- '.format(n),bin(n).replace("0b", ""))
