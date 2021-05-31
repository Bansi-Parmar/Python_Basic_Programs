## 11. A function f is defined as follows:
##     f(x) = ax3 – bx2 + cx –d, if x > k
##     = 0, if x = k
##     = -ax3 + bx2 - cx +d, if x < k
##     Write a program that reads a, b, c, d, k and x and prints the value of f(x).

print('\n\t Formula :- ax3 – bx2 + cx –d')
print('\t..............................\n')

(a,b,c,d,x,k) = (int(input("A :- ")),int(input("B :- ")),int(input("C :- ")),int(input("D :- ")),int(input("X :- ")),int(input("K :- ")))

if(x > k):
       print("f(x) = ",(a*(x**3))-(b*(x**2))+(c*x)-d)
elif(x == k):
       print("f(x) = 0")
elif(x < k):
       print("f(x) = ",(-a*(x**3))+(b*(x**2))-(c*x)+d)
       

                                        
                                     

