## 9. To find the maximum number out of given three positive numbers.

print('\n\t Find the maximum number')
print('\t..........................\n')


(n1,n2,n3) = (int(input("n1 :- ")),int(input("n2 :- ")),int(input("n3 :- ")))

if(n1 == n2 == n3):
       print("All three numbers are equal")
elif((n1 == n2) or (n3 == n2)or(n1 == n3)):
       if((n1 > n3)or(n1 > n2)):
              print("{} is the maximum number".format(n1))
       elif((n1 < n3)):
              print("{} is the maximum number".format(n3))
       else:
            print("{} is the maximum number".format(n2))
elif(n1 != n2 != n3):
       if((n1 > n2) and(n1 > n3)):
              print("{} is the maximum number".format(n1))
       elif((n2 > n1) and (n2 > n3)):
              print("{} is the maximum number".format(n2))
       elif((n3 > n1) and (n3 > n2)):
              print("{} is the maximum number".format(n3))
      
