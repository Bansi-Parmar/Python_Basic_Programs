## 29. To find factorial of a given number. N! = 1*2*3*…. *N.

print('\n\t factorial of a given number')
print('\t..............................\n')

no = int(input("Enter Number :- "))

def fact(n):
       if(n == 0):
              return 1
       return n * fact(n-1)

print("factorial of a given number is :- ".format(no),int(fact(no)))

