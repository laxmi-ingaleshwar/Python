#TYPES OF ARGUMENTS
'''
1.Positional Argument
2.Default Argument
3.Keyword Argument
4.Variable-length Argument

'''


#1
'''
def positional(name,phno,address,marks):
    print('name is:',name)
    print('phno is:',phno)
    print('address is:',address)
    print('marks is:',marks)
positional('lax',1234567890,'bgk',90)
'''

#2
'''
def default(name,phno1,phno2=none,address=none):
    print('name is:',name)
    print('phno1 is:',phno1)
    print('phno2 is:',phno2)
    print('address is:',address)
default('lax',1234567890,)
'''

#3
'''
def keyword(name,phno1,phno2,address):
    print('name is:',name)
    print('phno1 is:',phno1)
    print('phno2 is:',phno2)
    print('address is:',address)
keyword(address='banglore',name='laxx',phno1='987654321',phno2='1234567890')
'''    

#4
'''
def sample(*args):
    print(args)
sample(1,2,3,4,5,6,7,8)


def sample2(**kwargs):
    print(kwargs)
sample2(a=10,b=20,c=30,d=40)
'''


#Unpacking
'''
l=[1,2,3,4,5]
def sam(a,b,c,d,e):
    print(a+b+c+d+e)
sam(*l)
'''
#scope of variables
#global--> create outside the function& can be accesed
# -out and in,| *local--> create inside the function
#- can be accessed only in inside
'''
a=50
b=100
print('outside the function before modification:',a,b)
def scope():
    global a
    a = 500
    print('inside the function:',a,b)
scope()
print('outside the function after modification:',a,b)
'''


'''
a=50
b=100
print('outside the function before modification:',a,b)
def scope():
    global a,x,y
    a = 500
    x = 20
    y = 40
    print('inside the function:',a,b,x,y)
scope()
print('outside the function after modification:',a,b)
print(x,y,'outside')
'''

'''
a=10
b=20
def outer():
    x=30
    y=40
    a=500
    print('from outer function')
    print('global:',a,b)
    print('local before:',x,y)
    def inner():
        nonlocal x
        x=400
        m=100
        n=200
        print('from inner function')
        print('global:',a,b)
        print('local:',m,n)
        print('enclosing:',x,y)
    inner()
    print('local after modification:',x,y)
outer()
'''














