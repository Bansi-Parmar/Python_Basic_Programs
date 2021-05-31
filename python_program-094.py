## 94. To print ASCII value of all characters.

print('\n\t ASCII value of all characters')
print('\t................................\n')

for i in range(1,27):
       print('{} :- '.format(chr((i+64))),ord(chr(i+64)),end='   ')
       print('{} :- '.format(chr((i+96))),ord(chr(i+96)))
       



       
