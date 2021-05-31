## 120. You are given two 4-digit positive integers. Write a program to calculate
##      and print out the sum of the products of each pair of digits occupying
##      the same position in the two numbers. For example, if first number is
##      3445 and second number is 4534, then output will be 64
##      (3*4+4*5+4*3+5*4=64).

print('\n\t n1=3445,n2=4534 then ans=(3*4+4*5+4*3+5*4=64)')
print('\t................................................\n')

n1 = int(input('Enter 4-digit positive integers N1 :- '))
n2 = int(input('Enter 4-digit positive integers N2 :- '))
s=0;
if((len(str(n1))) == 4 and (len(str(n2)))== 4):
       for i in range(4):
              s = s+((n1%10)*(n2%10))
              n1=n1//10
              n2=n2//10
       print(s)
else:
       print('Please Enter 4-digit positive integers.')
