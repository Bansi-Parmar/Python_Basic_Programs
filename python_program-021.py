## 21. To print first 100 odd numbers. Note that program should display only
##     five numbers per line.

print('\n\t first 100 odd numbers')
print('\t........................\n')

for i in range(1,200):
    if(i%2 != 0):
        print(i,end=' , ')
    if(i%10==0):
        print()
        



