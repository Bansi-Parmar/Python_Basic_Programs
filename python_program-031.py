## 31. To print first 100 alternative odd numbers.

print('\n\t first 100 alternative odd numbers')
print('\t....................................\n')

no = int(input("Enter No:- "))

for n in range(1, no + 1):
    if(n % 2 != 0):
        print(n)

