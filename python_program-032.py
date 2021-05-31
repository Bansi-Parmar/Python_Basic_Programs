## 32. To print all odd numbers between V1 and V2. Assume that both V1 and V2
##     are positive and V1<V2.

print('\n\t print all odd numbers between V1 and V2')
print('\t..........................................\n')

v1 = int(input("Enter minimum value :- "))
v2 = int(input("Enter maximum value :- "))
if(v1 >= v2):
       print("Please Enter Valid data...")
else:
       for n in range(v1, v2 + 1):
           if(n % 2 != 0):
               print(n)

