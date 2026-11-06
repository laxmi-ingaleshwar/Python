
#1st type
'''
def sum():
    n1=int(input('Enter number:'))
    n2=int(input('Enter number:'))
    print (n1+n2)
sum()
'''

#wap to reverse a string
'''
def reverse():
    s=input('enter a string:')
    rev=''
    for i in s:
        rev=i+rev
    print(rev)
reverse()
'''
#2nd type of functions
'''
def add(n1,n2):
    print(n1+n2)
add(10,20)
'''

#wap to find the factorial of a number
'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial()
'''

#3rd type
'''
def sam():
    n1=int(input('enter:'))
    n1=int(input('enter:'))
    return n1+n2,n2-n1
a=sam()
print(a)
'''

# wap to check whether a num is prime or not
'''
def is_prime():
    n=int(input('enter a number:'))
    for i in range(2,n):
        if n%i==0:
            return f'{n} is not prime'
    return f'{n} is a prime number'
'''   

#4th type
'''
def sum(a,b):
    return a+b
print(sum(10,20))
'''

#wap to remove duplicates from list
'''
def remove_duplicates(l):
    out=[]
    for i in l:
        if i not in out:
            out.append(i)
    return out
print(remove_duplicates(eval(input("enter:"))))
'''

#wap to check whether num is perfect number/not
'''
def is_perfect(n):
    sum_factors=0
    for i in range(1,n):
        if n%i==0:
            sum_factors+=i
    return sum_factors==n
'''

#wap to check whether num is strong / not
#using while loop
'''
def is_strong(n):
    sum=0
    temp=n
    while n>0:
        d=n%10
        fact=1
        for i in range(1,d+1):
            fact*=i
        sum+=fact
        n//=10
    return sum==temp
'''

#using for loop
'''
def is_strong(n):
    sum=0
    for d in str(n):
        fact=1
        for i in range(1,int(d)+1):
            fact*=i
        sum+=fact
    return sum==n
'''

#nested function
'''
def factorial(n):
    fact=i
    for i in range(1,n+1):
        fact*=i
    return fact

def is_strong(n):
    sum=0
    for d in str(n):
        sum+=factorial (int(d))
    return sum==n
'''
# wap tprint strong num between 1 to 10000
'''
def strong_numbers():
    for i in range(1,10001):
        if is_strong(i):
            print(i)

'''

 



















