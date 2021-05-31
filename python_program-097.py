## 97. To print the series : 1, -2, 3, -4, 5, -6, 7, ….

print('\n\t 1, -2, 3, -4, 5, -6, 7, …')
print('\t............................\n')

no = int(input("Enter Number :- "))
arr = []
for i in range(1,no+1):
       if(i%2 == 0):
              arr.append(-i)
       else:
              arr.append(i)
print(*arr,sep=' , ')

##another way       
##for i in range(1,no+1):
##       if(i%2 == 0):
##              print(-i,end=' , ')
##       else:
##              print(i,end=' , ')



       
