## 4. An electronic component vendor supplies three products : transistors,
##     resistors and capacitors. The vendor gives a discount of 10% on orders
##     for transistors if the order is for more than Rs. 1000. On orders of more
##     than Rs. 100 for resistors, a discount of 5% is given, and a discount of
##     10% is given on orders for capacitors of value more than Rs. 500. Assume
##     that the numeric codes 1,2 and 3 are used for transistors, capacitors and
##     resistors respectively. Write a program that reads the product code and
##     the order amount and prints out the net amount that the customer is
##     required to pay after discount.

print('\n\t Net Amount')
print('\t............\n')

print('(1)Transistors  \n(2)Capacitors \n(3)Resistors ')

code = int(input('Select Product Code:- '))
amt = int(input("Enter Order amount :- "))

if(code > 3):
       print("Invalid choice ")
elif((code == 1) and (amt > 1000)):
       print("Net amount is :- ",int(amt-((amt*10)/100)))
elif((code == 2) and (amt > 500)):
       print("Net amount is :- ",int(amt-((amt*10)/100)))
elif((code == 3)and (amt > 100)):
       print("Net amount is :- ",int(amt-((amt*5)/100)))
else:
       print("Net amount is :- ",amt)
       
       
