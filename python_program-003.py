## 3. Write a program to do the following operations :
##     - Read any two positive integer operands (say op1 & op2) and one
##     character type operator (say opr). Note that opr is any mathematical
##     operator.
##     - Depending upon the operator, do the appropriate operation. e. g. if opr
##     is ‘+’ then the display the value obtained by evaluating the expression
##     (op1 + op2).

print('\n\t\t\t\t\t Menu Driven Program')
print('\t\t\t\t\t.....................\n')

print('Give Two integer number')
print('=======================\n')

op1 = int(input("Enter First  No :- "))
op2 = int(input("Enter Second No :- "))

print('\n Select Any One')
print('=================')
print(' + \n - \n * \n / \n %')

ch = input()

if(ch == '+'):
       print("Addition of Two number :- ",op1+op2)
elif(ch == '-'):
       print("Subtraction of Two number :- ",op1-op2)
elif(ch == '*'):
       print("Multiplication of Two number :- ",op1*op2)
elif(ch == '/'):
       print("Division of Two number :- ",int(op1/op2))
elif(ch == '%'):
       print("Module of Two number :- ",op1%op2)
else:
       print("Invalid choice ")
       
