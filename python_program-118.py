## 118. To calculate the sum of every third integer, beginning with i=2 (i.e.
##      calculate the sum 2+5+8+11+…) for all values of i that are less than 100.

print('\n\t 2+5+8+11+...+98')
print('\t..................\n')
s=0
for i in range(2,100,3):
       s = s + i
print(s)

