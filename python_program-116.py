## 116. To check whether the given number is an octal number or not.

print('\n\t Number is Octal or NOT')
print('\t..........................\n')

try:
       n = int(input("Enter Octal Number :- "),8)
       print('{} is Octal'.format(oct(n).replace("0o", "")))
except ValueError:
       print('Not Octal Number...')

