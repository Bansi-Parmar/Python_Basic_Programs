## 23. To compute the sum of each digits from a given positive integer number.

print('\n\t sum of each digits')
print('\t.....................\n')

no = int(input("Enter Number :- "))
n=no
##s=0
so=str(no)
##for n in range(len(str(no))):
##       s = s + int(no % 10)
##       no = no / 10

##print("Sum of each digit of {} :- ".format(n),int(s))
print("Sum of each digit of {} :- ".format(n),sum(map(int,so.strip())))
