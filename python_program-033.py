## 33. To find sum of all digits from a given positive number.

print('\n\t sum of all digits')
print('\t.....................\n')

no = int(input("Enter Number :- "))
s=0
for n in range(len(str(no))):
       s = s + int(no % 10)
       no = no / 10

print("Sum of {} :- ".format(no),int(s))

