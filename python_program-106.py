## 106. To evaluate the following sum:
##      sum =  (-1)n ((x n/2 )/n)(n+1) for n = 1 to 10


print('\n\t (-1)n ((x n/2 )/n)(n+1) for n = 1 to 10')
print('\t..........................................\n')

x = int(input("Enter x :- "))
s=0
for n in range(1,11):
    s = s + (((-1)**n)*((x**(n/2))/n)*(n+1))
print(s)
       
