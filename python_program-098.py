## 98. A pattern is constructed by stacking up 3 basic triangles formed with
##     stars. The figure below shows each basic triangle having 3 layers of stars:
##            *
##          * * *
##        * * * * *
##        *       *
##      * * *   * * *
##    * * * * * * * * *
 
print('\n\t pattern')
print('\t..........\n')

for r in range(1,6,2):
       print(('*'*r) .center(10))

for r in range(1,5,2):
       for c in range(2):
              if(r == 1):
                     print(' ',end=' ')
              if(r == 3):
                     print(' ',end='')
              print(('*'*r).center(2),end='')
       print()
print(('*'*9).center(2),end='')




       
