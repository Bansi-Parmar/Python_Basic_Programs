## 117. To check whether the given number is a binary number or not.

print('\n\t Number is Octal or NOT')
print('\t..........................\n')

try:
       n = int(input("Enter Octal Number :- "),2)
       print('{} is Binary Number'.format(bin(n).replace("0b", "")))
except ValueError:
       print('Not Binary Number...')

