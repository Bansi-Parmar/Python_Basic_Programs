## 24. To read any five real numbers and print the average value.

print('\n\t average value in given 5 numbers')
print('\t...................................\n')

no = []
for i in range(5):
       n = int(input("Enter {} Number :- ".format(i+1)))
       no.append(n)

print("average value :- ",sum(no) / len(no))

