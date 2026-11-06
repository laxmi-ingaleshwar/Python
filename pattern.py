#
'''for i in range(1,4):
    for j in range(1,4):
        print('*',end=' ')
    print()'''

# output:
#  ***
#  ***
#  ***



#
'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

# output:
#*    
# *   
#  *  
#   * 
#    *



#
'''for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

# output:
#*****
# ****
#  ***
#   **
#    *



#
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

# output:
#enter a number:6
#      *
#     * 
#    *  
#   *   
#  *    
# *


#
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()'''

#output:

#enter a number:7
#1      
#12     
#123    
#1234   
#12345  
#123456 
#1234567

#
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    ch=ord('A')
    for j in range(1,n+1):
        if i>=j:
            print(chr(ch),end=' ')
            ch+=1
        else:
            print(' ',end=' ')
    print()'''

# output:

#enter a number:9
#A                 
#A B               
#A B C             
#A B C D           
#A B C D E         
#A B C D E F       
#A B C D E F G     
#A B C D E F G H   
#A B C D E F G H I




#
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

#output:
   
#enter a number:7
#* * * * * * * 
#*           * 
#*           * 
#*           * 
#*           * 
#*           * 
#* * * * * * * 




#
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==n//2+1 or j==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

# output:
'''enter a number:7
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * * 
*     *     * 
*     *     * 
* * * * * * *
'''



# *rectangle with middle star
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==n//2+1 and i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

# output:

'''
enter a number:9
* * * * * * * * * 
*               * 
*               * 
*               * 
*       *       * 
*               * 
*               * 
*               * 
* * * * * * * * * 
'''


# X pattern
'''
n=int(input('enter a number:'))

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j== n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''

#output:

'''
enter a number:5

*       * 
  *   *   
    *     
  *   *   
*       * 
'''


# if col is even number print square of it
'''
for i in range(1,6):
    for j in range(1,i+1):
        if j%2==0:
            print(j**2 ,end=' ')
        else:
            print(j ,end=' ')
    print()
    '''

#output:
'''   
1 
1 4 
1 4 3 
1 4 3 16 
1 4 3 16 5 
     '''

#pyramid
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,((n*2)-1)+1):
        if i==n or i+j==n+1 or j-i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#output:
'''   
enter a number:6
          *           
        *   *         
      *       *       
    *           *     
  *               *   
* * * * * * * * * * * 
'''

#
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for s in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')
    print()
'''
#OR
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*(i))
'''

#output:
'''
enter a number:5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

#
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for s in range(n-i):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')
    print()
for i in range(1,n):
    for s in range(i):
        print(' ',end='')
    for j in range(n-i):
        print('* ',end='')   
    print()

'''

#OR
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    print(' '*(n-i)+'* '*(i))
for i in range(1,n):
    print(' '*(i)+'* '*(n-i))
'''

#output:
'''
enter a number:5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    *
''' 

#
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()


for i in range(1,n+1):
    ch=ord('A')
    for j in range(1,n+1):
        if j>=i:
            print(chr(ch),end=' ')
            ch+=1
        else:
            print(' ',end=' ')
    print()
    

for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print(i,end=' ')
        else:
            print(' ',end=' ')
    print()
    

for i in range(1,n+1):
    k=ord('A')+i-1
    for j in range(1,n+1):
        if i+j<=n+1:
            print(chr(k),end=' ')
            k+=1
        else:
            print(' ',end=' ')
    print()
'''

# A pattern
'''
n=int(input('enter a number:'))

for i in range(1,n+1):
    for j in range(1,n+1):
        if (j==1 and i!=1)or(j==n and i!=1)or (i==1 and 1<j<n) or i==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#output:
''' 
enter a number:5
  * * *   
*       * 
* * * * * 
*       * 
*       * 
'''




# B pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1  or (j==n and i!=1)or (i==1 and 1<j<n) or i==n or i==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#C pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or (j==1 and i!=1) or i==n or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#D pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#output:


#E pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1  or (i==1 and 1<j) or (i==n and 1<i) or i==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#output:
'''
enter a number:5
* * * * * 
*         
* * * * * 
*         
* * * * * 
'''

# F pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''

#output:
'''
enter a number:5
* * * * * 
*         
* * * * * 
*         
* 
'''

# G pattern

# H pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#output:
'''
enter a number:5
*       * 
*       * 
* * * * * 
*       * 
*       * 
'''

# I pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#output:
'''
enter a number:5
* * * * * 
    *     
    *     
    *     
* * * * * 
'''
# J pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

# K pattern

# L pattern
'''
n=int(input('enter a number:'))
for i in range(1,n):
    for j in range(1,n):
        if j==1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#output:
'''
enter a number:6
*         
*         
*         
*         
* * * * * 
'''

# N pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
#output:
'''
enter a number:5
*       * 
* *     * 
*   *   * 
*     * * 
*       * 
'''

# O pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j==1 and 1<i<n) or (i==n and 1<j<n) or (j==n and 1<i<n) or (i==1 and 1<j<n):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#output:
'''
enter a number:5
  * * *   
*       * 
*       * 
*       * 
  * * *   
'''

# T pattern
'''
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==n//2+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#output:
'''
enter a number:5
* * * * * 
    *     
    *     
    *     
    *   
'''




    

