## 95. To print the series : 2, 10, 30, 68, 130, ….

print('\n\t 2, 10, 30, 68, 130, …')
print('\t........................\n')

no = int(input("Enter Number :- "))
arr = []
for i in range(1,no+1):
       arr.append((i*i*i)+i)
print(*arr,sep=',')

## another way
##for i in range(1,no+1):
##       print((i**3)+i,end=' , ')      
       



       
