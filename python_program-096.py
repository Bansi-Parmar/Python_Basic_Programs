## 96. To print the series : 1, 3, 6, 10, 15, 21, ….

print('\n\t 1, 3, 6, 10, 15, 21, …')
print('\t........................\n')

no = int(input("Enter Number :- "))
arr = []
temp=0
for i in range(1,no+1):
       temp = temp + i
       arr.append(temp)
print(*arr,sep=',')

##another way...
##t=0
##for i in range(1,no+1):
##       print(t+i,end=' , ')
       



       
