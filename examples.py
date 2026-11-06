#sum of 2 values
'''x=int(input("enter a value of x:"))
y=int(input("enter a value of y:"))
print('the sum is',x+y)'''

#area of rectangle
'''l=eval(input("enter value of length:"))
w=eval(input("enter value of width:"))
print('area of rectangle',length*width)'''

#reverse a string
'''string=(input("enter a string:"))
print('reversed of the string is:',string[::-1])'''

#check whether eligible or not to vote
'''age=int(input('enter your age:'))
if age>=18:
    print('you are eligible')'''

#perimeter of square
'''side=eval(input('enter length of one side of square:'))
print('perimeter of the square is:',side*4)'''

#check whether number is positive
'''num=int(input('Enter a number:'))
if num >=0:
    print('positive')'''

#WAPTP square of int number if it is even
'''num=int(input('enter a number:'))
if num%2==0:
        print('num','is even and its square is',num**2)'''

#check whether a char is vowel or not
'''s=input('enter a alphabet:')
if s in('a','e','i','o','u'):
    print(s,'Alphabet is vowel')'''

'''ch=input('enter a char:')
if ch in 'aeiouAEIOU':
    print(ch,'is vowel')'''


#waptp the square of a number if it is even else
#print cube of it
'''num=int(input('enter a number:'))
if num%2==0:
    print('num','is even and its square is:',num**2)
else:
    print('num','is odd and cube is:',num**3)'''


#whether check char is alphabet /not
'''ch=input('enter a character:')
if ch>='A' and ch<='Z':
#if 'A'<=ch<='Z':
    print('Character is Uppercase:')
else:
    print('Character is not Uppercase:')'''


#whether number is divisible by both 3 and 5
'''n=int(input('enter a number:')) 
if n%3==0 and n%5==0:
    print(f'{n}is divisible by both 3 and 5')
else:
    print('number is not divisible')'''

    
#whether char is digit/not
'''n=int(input('enter a character:'))
if n>=0<=9:
    print('character is digit')
else:
    print('character is not digit')'''

#whether word keyword/not
'''import keyword
ch=input('enter a Character:')
if keyword.iskeyword(ch):
    print(f'{ch} is a Keyword')
else:
    print(f'{ch} is not a keyword')'''

'''s=input('enter a word:')
import keyword
if s in keyword.kwlist:
    print(s,'is a keyword')
else:
    print(s,'is not a keyword')'''

#special character/not
'''s=input('enter a word:')
if not (s>='a'and s<='z' or s>='A' and s<='Z' or s>='0' and s<='9'):
    print(s,'Character is special')
else:
    print(s,'character is not special')'''

'''ch=input('enter a word:')
if'''

#to check whether a string is polindrome or not
'''s=input('enter a word:')
if s==s[::-1]:
    print(s,'is a polindrome')
else:
    print(s,'is not polindrome')'''
    
#waptc whether the data is mutable or not
'''a=eval(input('enter a word:'))
if type'''

#whether 2 values are pointing to the same memory/not
'''v1=eval(input('enter:'))
v2=eval(input('enter:'))
if id(v1)==id(v2):
    print(v1,v2,'are pointing to the same memory')
else:
    print(v1,v2,'are not pointing to the same memory')'''

#whether data is mutable/not
'''d=eval(input('enter the data:'))
if type(d) in [list,set,dict]:
    print('mutable')
else:
    print('immutable')'''
#whether the list contain middle value /not
'''l=eval(input('enter:'))
if len(l)%2==1:
    print(l,'contains mid value and the value is',l[len(l)//2])
else:
    print(l,'no mid value')'''

#check whether a char is upper,lower,digit /special char
'''ch=input('enter a character:')
if 'A'<=ch<='Z':
    print(ch,'upper case')
if 'a'<=ch<='z':
     print(ch,'lower case')
if '0'<=ch<='9':
     print(ch,'digit')
else:
    print(ch,'special character')'''

#check whether the number is single/double /triple /more than three digit
'''n=abs(int(input('Enter a Number:')))
if 0<=n<=9:
    print(n,'is a single digit')
elif 10<=n<=99:
    print(n,'is a double digit')
elif 100<=n<=999:
    print(n,'is a triple digit')
else:
    print(n,'more than three digit')'''

#waptc the character is vowel/consonant
'''ch=input('enter a character:')
if 'A'<=ch<='Z' or 'a'<=ch<='z':
    if ch in 'AEIOUaeiou':
        print(ch,'Character is vowel')
    else:
        print(ch,'character is consonat')
else:
    print('not alphabet')'''
#waptp middle value of list if it is a polindrome string
l=eval(input('enter a list:'))
if len(l)%2!=0:
    mid=l[len(l)//2]
    if type(mid)==str:
        if mid==mid[::-1]:
            print('the list contains a polindrome str as mid value',l[len(l)//2])
        else:
            print(mid,'is not a polindrome')
    else:
        print(mid,'is not a string')
else:
    print('the list does not have middle value')

#waptp the reversed string if it is starting with vowel and ending with special character
'''ch=input('enter a string:')
if ch[0] in'aeiouAEIOU':
    if not ('A'<=ch[-1]<='Z' or 'a'<=ch[-1]<='z' or '0'<=ch[-1]<='9'):
        print(ch[::-1],'str start with vowel and ends with special character')
    else:
        print('does not end with special character')
else:
    print('does not start with vowel')'''
        
        
