#lambda()
'''
even_odd=lambda num:num**2 if num%2==0 else num**3
print (even_odd(10))
'''

#map()
'''
l=[1,2,3,4,5]
square=lambda num:num**2

out=map(square,l)
print(list(out))
'''

#filter()
'''
l=[1,2,3,4,5]

even=lambda num:num%2==0
out=filter(even,l)
print(list(out))
'''

#----------------Comprehension-------------
# 1.-------list comprehension-----------

'''
# expression for item in iterable
nums=[num for num in range(1,11)]
print(nums)
'''
# expression for item in iterable if cond
'''
even_nums=[num for num in range(1,11) if num%2==0]
print (even_nums)
'''
# TSB if cond else FSB for item in iterable
'''
nums= [num**2 if num%2==0 else num**3 for num in range (1,11)]
print (nums)
'''


# wap to extract only str which starts with a

l=['apple','heaven','cake','animal','air']
#print([word for word in l if  word[0]=='a'])

l=['apple','heaven','cake','animal','air']
#print([word for word in l if word.startswith('a')])

# wap to replace negative numbers with 0
'''
l=eval(input('enter a list:'))
print([0 if num<0 else num for num in l])
'''

# wap to create list that contains len of words present in the input list
'''
l=['apple','heaven','cake','animal','air']
print ([len(word)for word in l])
'''

'''
l1=[1,2]
l2=[3,4]
print([(i,j) for i in l1 for j in l2])
'''
#output: [(1, 3), (1, 4), (2, 3), (2, 4)]


'''
l1=[4,5]
l2=[5,6]
print([(i,j) for i in l1 for j in l2])
'''
#out=[4,5,5,6]


#2.------------set comprehension----------

'''
s='donkey'
out={(0,'d'),(1,'o'),(2,'n')}
'''
#print({(i,s[i]) for i in range(0,len(s))})

#for i,j in enumerate(s):
 #   print(i,j)
'''
print({(i,j) for i,j in enumerate(s)})

'''

#3.------------- dict comprehension---------------
'''
l1=[1,2,3,4]
l2=[5,6,7,8,9]
for (i,j) in zip(l1,l2):
    #print(i,j)
'''
#out:
    
'''
1 5
2 6
3 7
4 8
'''


l=['apple','heaven','cake','animal','air']
#print ({word: len(word) for word in l})

#out: {'apple': 5, 'heaven': 6, 'cake': 4, 'animal': 6, 'air': 3}


s='heaven'
#print ({i:ord(i) for i in s if ord(i)%2==0})

#out: {'h': 104, 'v': 118, 'n': 110}


l1=[1,2,3]
l2=[4,5,6]
#out{1:4,2:5,3:6}
#print ({i:j for i,j in zip(l1,l2)})



l1=[23,4.5,'hii',[1,2,3],100]
l2=[5,10,15,20,[1,2,3]]
#print ({i:j for i,j in zip(l1,l2) if type (i) not in [list,set,dict]})

#out: {23: 5, 4.5: 10, 'hii': 15, 100: [1, 2, 3]}


l=['hii','dad','mom','pink','cherry']
out={'hii':'iih','dad': 3, 'mom':3, 'pink':'knip','cherry': 'yrrehc'}
#print({word:len(word) if word==word[::-1] else word[::-1] for word in l}) 

#{'hii': 'iih', 'dad': 3, 'mom': 3, 'pink': 'knip', 'cherry': 'yrrehc'}


#--------ITERATOR-------
'''
var=iter(iterable)
next(var)


l=[1,2,3,4,5]
a=iter(l)
next(a)
1
next(a)
2
next(a)
3
next(a)
4
next(a)
5
next(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    next(a)
StopIteration
'''

#-------GENERATOR-------------
# yield keyword- generate one value at a time
def sam():
    a=10
    b=20
    yield a+b
    yield a-b
    yield a*b
#print(list(sam()))
i=iter(sam())

'''
[30, -10, 200]

next(i)
30
next(i)
-10
next(i)
200
next(i)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    next(i)
StopIteration
'''

def sam():
    a=10
    b=20
    print('hello everyone')
    yield a+b
    print('happy deepavali')
    yield a-b
    print('monday & tuesday is holiday')
    yield a*b
#print(list(sam()))
i=iter(sam())

'''
list(sam())
hello everyone
happy deepavali
monday & tuesday is holiday
[30, -10, 200]
next(i)
hello everyone
30
next(i)
happy deepavali
-10
next(i)
monday & tuesday is holiday
200
next(i)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    next(i)
StopIteration
'''

#wap to extract all the even numbers from list

def even_nums(l):
    even=[]
    for i in l:
        if i%2==0:
            even.append(i)
#    print(even)
even_nums([1,2,3,4,5,6,7,8,9])


def even_nums(l):
    for i in l:
        if i%2==0:
            yield i
#print(list(even_nums([1,2,3,4,5,6,7,8,9])))



import sys
gen=(i for i in range(1,1000))
com=[i for i in range(1,1000)]
#print(sys.getsizeof(gen))
#print(sys.getsizeof(com))









