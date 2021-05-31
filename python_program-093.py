## 93. A diamond pattern is formed with a given letter of the alphabet. Write a
##     program to generate and display such by accepting any character and
##     total number of lines (say N). Assume N is an odd number.
##     For example, if the accepted character is ‘X’ and N = 7, then your program
##     should display the following output :
##       X
##      X X
##     X X X
##    X X X X
##     X X X
##      X X
##       X

print('\n\t diamond pattern')
print('\t..............\n')

n = int(input("Enter OOD Number :- "))
fact=1
if(n%2 == 0):
       print('{} is NOT a Valid ODD Number'.format(n))
else:
       for r in range(n):
              print(('x '*r) .center(n*3))
       for r in range(n,0,-1):
              print(('x '*r) .center(n*3))

       
