## 22. To print multiplication table from 1x1 to 10x10.

print('\n\t multiplication table from 1x1 to 10x10')
print('\t.........................................\n')

for i in range(1,11):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print("-"*20)
