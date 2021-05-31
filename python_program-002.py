## 2. To find out simple interest using the following formula:
##     I = (P * R * N) / 100
##     where P = principal amount,
##     R = Rate of interest and
##     N = Number of year.

print('\n\tCalculate the Simple Interest')
print('\t..............................\n')

p = int(input("Enter P (principal amount):- "))
r = int(input("Enter R (Rate of interest):- "))
n = int(input("Enter N (Number of year):- "))

print("simple interest (I) :- ",(p * r * n) / 100)

# show only integer format
##print("simple interest :- ",int((p * r * n) / 100))
