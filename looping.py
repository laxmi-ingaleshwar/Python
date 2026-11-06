
'''i=1
while i<=100:
    print('hello')
    i=i+1'''
#number from 1 to 10
'''i=1
while i<=10:
    print (i)
    i=i+1'''

#waptp numbers from 10 to 1
'''i=10
while i>=1:
    print(i)
    i=i-1'''
#waptp the even numbers between 1 to n
'''n=int(input('enter a number:'))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i=i+1'''

'''n=int(input('enter a number:'))
i=2
while i<=n:
    print(i)
    i=i+2'''
#waptp the factors of a number
'''n=int(input('enter a number:'))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i=i+1'''

'''n=int(input('enter a number:'))
i=1
while i<=n/2:
    if n%i==0:
        print(i)
    i=i+1
print(n)'''

#wap to find the sum of n natural numbers
'''n=int(input('enter a number:'))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(sum)'''
#wap to find product of n natural/ factorial of number
'''n=int(input('enter a number:'))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print(fact)'''
#wap tp multiplication table of a given number
'''n=int(input('enter:'))
i=1
while i<=10:
    print(f'{n} X {i} = {n*i}')
    i=i+1'''

#sum of even numbers betn 1 to 100
'''n=int(input('enter:'))
i=1
sum=0
while i<=100:
    if i%2==0:
        sum=sum+i
print(sum,s)'''

#product of odd numbers betn 1 to 50
'''i=1
product=1
while i<50:
    product*=i
    i=i+2
print(product)'''

#whether number is perfect/not
'''n=int(input('enter:'))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if sum==n:
    print(n,'is a perfect number')
else:
    print(n,'is not a perfect number')'''
#wap to count number of digits presents in a number
'''=int(input('enter:'))
count=0
while n > 0:
    n = n //10
    count=count+1
print('number of digits:',count)'''

# find the sum of all digits presents
'''n=int(input('enter:'))
sum=0
while n>0:
    d=n%10
    sum+=d
    n=n//10
print(sum)'''

#wap to reverse a number
'''n=int(input('enter:'))
rev=0
while n >0:
    d=n%10
    rev = (rev*10) + d
    n=n//10
print(rev)'''

#wap to polindrome
'''n=int(input('enter:'))
temp=n
rev=0
while n >0:
    d=n%10
    rev = (rev*10) + d
    n=n//10
    print(rev)
if rev == temp:
    print('polindrome')'''

# wap to convert int into binary
'''n=int(input('enter:'))
rev =0
while n>0:
    d=n%2
    rev= (rev+i) +d
    n=n//10
    print('')'''

# binary into int
'''n=int(input('enter:'))
rev =0
while n>0:
    d=n%2
    rev= (rev*2)+d
    n=n//10
print(rev)'''

#print all the numbers which are multiple of 5 from 1 to n

#ptp numbers from n to 1
'''n=int(input('enter:'))

while n>=1:
    print(n)
    n=n-1'''
#p to print sum of individual digit
'''n=int(input('enter:'))

sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
print(sum)'''

#find the sum of n natural numbers
'''n=int(input('enter:'))
sum=0
i=1

while i<=n:
    sum=sum+i
    i=i+1
print(sum)'''

#p to print every char from string

#wapt extract the even integers that present in odd index of list.
'''l=eval(input("enter a list:"))
out=[]
for i in range(1,len(l),2):
    if type(l[i])==int:
        if l[i]%2==0:
            out.append(l[i])
print(out)'''

#
'''s='hello'
out={}
for i in range (len(s)):
    out[i]=s[i]
print(out)'''




#wap to get following
'''l=['jiocinema.com','file.py','web.html','amazon.com','www.org','python.py']
out={}

for i in l:
    a=i.split('.')
    if a[1] not in out:
        out.append(a[1])
print(out)'''

#
'''s='you have pre-mock today'
res={}
for word in words:
    if len(word)%2==0:'''
        

#
'''s='you have pre-mock today'
longest_word=''
for word in s.split():
    if len (word) > len(longest_word):
        longest_word=word
print(longest_word)'''

#
'''s='10100011231'
out=''
for i in s:
    if i=='1':
        out+='0'
    elif i=='0':
        out+='1'
print(out)'''

#
'''l=['jio,com','file.py','web.html','amazon.com','www.org','python.py']'''

# find the greatest number present in a list
'''numbers=[12,34,123,56,78,90,456,23,67]
greatest=0

for num in numbers:
    if num> greatest:
        greatest=num
print(greatest)'''

#
'''numbers=[12,34,123,56,78,90,456,23,671,670,672,700,750]
greatest=0
s_greatest=0

for num in numbers:
    if num>greatest:
        s_greatest=greatest
        greatest=num
    elif num > s_greatest and num!=greatest:
        s_greatest = num
        
print(s_greatest)'''

#
'''s=input('enter a string:')
for i in s:
      if s.count(i)==1:
        print(i)
        break
else:
    print('there is no repeating character')'''
#check whether the str contains only lowercase
'''s=input('enter a string:')
for i in s:
    if not('a'<=i<='z'):
        print('str contain other than lower case char')
        break
else:
    print('str contain only lower case char')'''

#check whether a tuple is homogeneous or not
#wap to find first repeated char

#numbers between 1 to 50 which % both 3 & 5

'''for i in range(1,10,2):
    for j in range(1,10,3):
        print(i,j)'''

'''c=0
for i in range(1,15,3):
    for j in range(2,20,4):
        for k in range(5,50,10):
            print(i+j+k)
            c+=1'''

#wap to flatten a nested list
'''l=[[1,2,3],[4,5,6],[7,8,9]]
out=[1,2,3,4,5,6,7,8,9]
flatten_list=[]
for i in l:
    for j in i:
        flatten_list.append(j)
print(flatten_list)'''


#wap  to get following 
'''s='power star'
out={}
for i in s.split():
    count=0
    for j in i:
        count+=1
    out[i]=count
print(out)'''

#
'''s='power star'
out={}
for i in s.split():
    count=0
    for j in i:
        if j in 'AEIOUaeiou':
            count+=1
    out[i]=count
print(out)'''

#
'''s='power star'
out={}
for i in s.split():
    count=0
    for j in i:
        if j in 'AEIOUaeiou':
            count+=1
    out[i]=[i[::-1],count,i[::2]]
print(out)'''

#
'''
l=['hello',227,3.4,'last',189,34]
out=[]
for i in l:
    if type(i)==int:
        rev=0
        while i>0:
            d=i%10
            rev=(rev*10)+d
            i//=10
        out.append(rev)
print(out)
'''  









