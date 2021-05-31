## 28. To calculate the sum of the square of first N numbers.

print('\n\t sum of the square of first N numbers')
print('\t.......................................\n')

no = int(input("Enter Number :- "))

s = 0
for i in range(1, no+1) :
       s = s + (i**2)

print("sum of the square of first {} numbers. is :- ".format(no),s)

