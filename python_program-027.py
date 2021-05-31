## 27. To calculate the average of first N even numbers.

print('\n\t average of first N even numbers')
print('\t.................................\n')

no = int(input("Enter Number :- "))
sm = 0
for i in range(2, no*2+1,2) :
       sm += i
##       print(i)
##print(sm)
print("average of first {} even numbers is :- ".format(no),sm/no)

