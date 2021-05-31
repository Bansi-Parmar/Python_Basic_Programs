## 10. Write a program that reads three positive numbers a, b, c and determines
##     whether they can form the three sides of a triangle. If yes, determine
##     whether the triangle will be an obtuse-angle, or a right-angle or an acuteangle
##     triangle. If the triangle is an acute angle triangle, determine further
##     whether the triangle is equilateral, isosceles or scalene.

print('\n\t triangle')
print('\t...........\n')


(a,b,c) = (int(input("A :- ")),int(input("B :- ")),int(input("C :- ")))


if(((a*a) > ((b*b) + (c*c))) or (((b*b) > ((a*a) + (c*c))) or (((c*c) > ((b*b) + (a*a)))))):
                               print("triengle is obtuse-angle")
elif(((a*a) == ((b*b) + (c*c))) or (((b*b) == ((a*a) + (c*c))) or (((c*c) == ((b*b) + (a*a)))))):
                                  print("triengle is right-angle")
elif(((a*a) < ((b*b) + (c*c))) or (((b*b) < ((a*a) + (c*c))) or (((c*c) < ((b*b) + (a*a)))))):
                                 print("triengle is acute-angle")
                                 if(a == b == c):
                                    print("equilateral")
                                 elif((a == b) or (b == c) or (c == a)):
                                        print("isosceles")
                                 elif(a != b != c):
                                        print("scalene")
                                        
                                     

