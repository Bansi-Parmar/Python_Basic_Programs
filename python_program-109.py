##     109. Write a program to do the following tasks:
##            [a] Read any two positive numbers say n1 & n2. Assume n1>n2.
##            [b] Print all even numbers that lies between n1 & n2.
##            [c] Print the total number of an even numbers between n1 and n2.


print('\n\t even numbers count')
print('\t......................\n')

n1 = int(input("Enter maximum value N1 :- "))
n2 = int(input("Enter minimum value N2 :- "))
c=0
if(n1 > n2):
       print('All even numbers between {} and {} are :- '.format(n1,n2))
       for i in range(n2,n1+1):
              if(i%2 == 0):
                     c+=1
                     print(i,end=' ')
       print()
       print('Total even numbers between {} and {} are :- '.format(n1,n2),c)

else:
       print('NOT a VALID Number')


       
