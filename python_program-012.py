## 12. Write a program that read three digited positive numbers and find the
##     sum of all digits from the given number. For example, if the input number
##     is 345, then the sum will be 12 (i. e. 3+4+5).

print('\n\t sum of three digited Number')
print('\t..............................\n')

d = int(input("Enter three digited numbers  :- "))
s = str(d)
if(len(s) == 3):
       print("sum of {} is :- ".format(d),sum(map(int,s.strip())))
else:
       print("Please Enter three digited positive numbers")
              
              

                                        
                                     

