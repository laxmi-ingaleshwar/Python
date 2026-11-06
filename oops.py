'''
class Human:
    eyes=2
    nose=1
    ear=2
    brain=1
    def __init__ (self,age,contact,addr,quali):
        self.age=age
        self.contact=contact
        self.addr=addr
        self.quali=quali
    def display(self):
        self.static()
        print(self.age,self.contact,self.addr,self.quali)
    @classmethod
    def update_age(self,new):
        self.age=new
    @classmethod
    @classmethod
    def cls_display(cls):
        cls.static()
        print(cls.eyes,cls.nose,cls.ear,cls.brain)
    @classmethod
    def update_brain(cls,new):
        cls.brain=new
    @staticmethod
    def static():
        print('The properties are:',end=' ')
        
Hita=Human(21,1234567890,'banglore','BCA')
Sayanth=Human(23,1987654321,'Mysoore','BE')
Harsh=Human(21,5432167890,'Bagalkot','BCA')
Hita.display()
Sayanth.display()
Harsh.display()
Human.cls_display()
Human.update_brain()
Human.update_age()
'''

'''
class bank:
    Bank_name='Canara'
    location='Vijaynagar'
    Bank_manager='Ansh'
    def __init__(self,name,accno,contact,balance):
        self.name=name
        self.accno=accno
        self.contact=contact
        self.balance=balance
    def deposit(self):
        dep=int(input('Enter deposit amount:'))
        self.balance += dep
        print('Amount Deposited successfully Rs='',dep)

    def withdrawal(self):
        wd =int(input('Enter withdrawal amount:'))
        self.balance -= wd
        print('')

    def display(self):
        print(self.name,self.accno,self.contact,self.balance)
cust1=bank('rani',123456789,2345678909,1000)
cust2=bank('ramya',23415679,56473899,2000)
cust1.display()
cust2.display()
cust1.deposit()
'''
#=======Pillars of OOps===============
#1.Inheritance
#2.Polymorphism
#3.Encapsulation
#4.Abstraction

#-------INHERITANCE---------------
#-------SINGLE LEVEL--> deriving properties from one parent class to one child class
'''
class Vehicle:
    brand='Suzuki'
    fuel_type='petrol'
    def start(self):
        print('the vehicle is starting')

class Bike(Vehicle):
    color='Black'
    price=150000
    model='BS4'
    wheels=2
    brand='dio'
    def ride(self):
        print('today im going to bike ride')
user1=Bike()
'''

#------MULTI LEVEL--> deriving properties from one derived class to another derived class

'''
class Resume_10:
    def __init__ (self,name,contact,email,per_10,yop_10,sname,board_10):
        self.name=name
        self.contact=contact
        self.email=email
        self.per_10=per_10
        self.yop_10=yop_10
        self.sname=sname
        self.board_10=board_10
        
    def display(self):
        print(self.name,self.contact,self.email,self.per_10,self.yop_10,self.sname,self.board_10,sep='\n')
        
    def update_contact(self,new):
        self.contact=new


                 
class Resume_12(Resume_10):
    def __init__(self,name,contact,email,per_10,yop_10,sname,board_10,per_12,yop_12,cname,board_12):      
        super().__init__(name,contact,email,per_10,yop_10,sname,board_10)
        self.per_12=per_12
        self.yop_12=yop_12
        self.cname=cname
        self.board_12=board_12

    def display(self):
        super().display()
        print(self.per_12,self.yop_12,self.cname,self.board_12)



class Resume_bca(Resume_12):
    def __init__(self,name,contact,email,per_10,yop_10,sname,board_10,per_12,yop_12,cname,board_12,cgpa,yop,college,university):
        super().__init__(name,contact,email,per_10,yop_10,sname,board_10,per_12,yop_12,cname,board_12)
        self.cgpa=cgpa
        self.yop=yop
        self.college=college
        self.university=university
        
    def display(self):
        super().display()
        print(self.cgpa,self.yop,self.college,self.university)
        

s1=Resume_bca('laxmi',1234567890,'lax@gmail.com',90,2021,'GVVS','KSSEB',88,2023,'GVVS','PUC',9.19,2026,'GFGC','BGK')
s1.display()      
#s1.display_10()
#s1.display_12()
#s1.display_bca()
'''


#-------MULTIPLE LEVEL--> Single Child inherits from n Number of Parents

'''

class Batsman:
    def __init__(self,name,team,age,runs,century):
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.century=century
    def bat(self):
        print(self.name,'is batting')
        return self

class Bowler:
    def __init__(self,name,team,age,wickets,dot_balls):
        self.name=name
        self.team=team
        self.age=age
        self.wickets=wickets
        self.dot_balls=dot_balls
    def bowl(self):
        print(self.name,'is bowling')
        return self

class AllRounder(Batsman,Bowler):
    def __init__ (self,name,team,age,runs,century,wickets,dot_balls):
        #super().__init__(wickets,dot_balls)
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.century=century
        self.wickets=wickets
        self.dot_balls=dot_balls
    def field(self):
        print(self.name,'is feilding')
        return self

ob=AllRounder('Krunal pandya','RCB',35,5000,20,100,4000)

#ob.bat()
#ob.bowl()
#ob.field()

ob.bat() .bowl() .field() #(return self)
print(AllRounder.mro())  #OR AllRounder.__mro__
'''
#MRO()--> first it derives properties from its own class & then respective mentioned parent class.

# -------- HIERARCHICAL INHERITANCE -------->
# Multiple Child classes inherit from Single Parent
'''
class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print(self.name, 'is eating')
        return self


class Dog(Animal):
    def bark(self):
        print(self.name, 'is barking')
        return self


class Cat(Animal):
    def meow(self):
        print(self.name, 'is meowing')
        return self


class Cow(Animal):
    def sound(self):
        print(self.name, 'is mooing')
        return self


d = Dog('Tommy', 3, 'Brown')
c = Cat('Kitty', 2, 'White')
co = Cow('Ganga', 5, 'Black')


d.eat().bark()
c.eat().meow()
co.eat().sound()

'''


# -------- HYBRID INHERITANCE -------->
# Combination of Multiple + Multilevel Inheritance

'''
class Cricketer:
    def __init__(self, name, team):
        self.name = name
        self.team = team
    def info(self):
        print(self.name, 'plays for', self.team)
        return self


class Batsman(Cricketer):
    def bat(self):
        print(self.name, 'is batting')
        return self


class Bowler(Cricketer):
    def bowl(self):
        print(self.name, 'is bowling')
        return self


class AllRounder(Batsman, Bowler):
    def field(self):
        print(self.name, 'is fielding')
        return self


ob = AllRounder('Krunal Pandya', 'RCB')
ob.info().bat().bowl().field()

print(AllRounder.mro())

'''

#--------------POLYMORPHISM----------------
#---METHOD OVERLOADING--> PYTHON DOESN'T SUPPORT
#---METHOD OVERRIDING--

'''
def sam(a,b):
    print(a+b)
temp1=sam
def sam(a,b,c):
    print(a+b-c)
temp2=sam
def sam(a,b,c,d):
    print(a+b,c+d)
sam(1,2,3,4)
temp1(10,20)
temp2(10,20,10)
'''


'''
class Parent:
    def sam(self):
        print(' im from parent class')

ob1=Parent()
class Child(Parent):
    def sam(self):
        print('im from child class')
    def child(self):
        print('hello everyone')
ob=Child()
ob=Parent()

ob.sam()
'''

#------duck typing--> way of achieving polymorphism,where type of an object
# is not important, instead it's behaviours[attributes/methods imp]
'''
class Dog:
    def sound(self):
        print('bow bow')

class Cat:
    def sound(self):
        print('meow meow')
c=Cat()
d=Dog()

def make_sound(obj):
    obj.sound()

'''   
'''
c.sound()
meow meow
d.sound()
bow bow

'''

#---OPERATOR OVERLOADING--------
'''
class Sam:
    def __init__(self,a):
        self.a=a
    # arithmetic operator
    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self,other):
        return self.a*other.a
    def __truediv__(self,other):
        return self.a/other.a
    def __floordiv__(self,other):
        return self.a//other.a
    def __mod__(self,other):
        return self.a%other.a
    def __pow__(self,other):
        return self.a**other.a

    #bitwise operator
    
    def __and__(self,other):
        return self.a&other.a
    def __or__(self,other):
        return self.a|other.a
    def __xor__(self,other):
        return self.a^other.a
    def __lshift__(self,other):
        return self.a<<other.a
    def __rshift__(self,other):
        return self.a>>other.a

    # relational operator

    def __eq__(self,other):
        return self.a==other.a
    def __ne__(self,other):
        return self.a!=other.a
    def __gt__(self,other):
        return self.a>other.a
    def __lt__(self,other):
        return self.a<other.a                                                  
    def __ge__(self,other):
        return self.a>=other.a
    def __le__(self,other):
        return self.a<=other.a


x=Sam(10)
y=Sam(20)

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

print(x&y)
print(x|y)
print(x^y)
print(x<<y)
print(x>>y)

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

'''




'''
class sam:
    def __init__(self,x):
        self.x=x
    def __len__(self):
        return len(self.x)
    def __getitem__(self,index):
        return self.x[index]
    def __setitem__(self,index,new):
        self.x[index]=new
    def __contains__(self,val):
        return val in self.x
    def __str__ (self):
        return 'object belongs to sam class'
    def __call__ (self):
        return 'object is being called'

ob=sam([1,2,3,4])

print(ob())
'''
'''
1 in ob
True
8 in ob
False
'''

#------------------ENCAPSULATION-----------
'''
class Bank:
    bname='SBI'
    __branch='vijaynagar'
    manager='Ravi'
    ifsc='sbi012902'
    def __init__(self,name,phno,accno,bal):
        self._name=name
        self.__phno=phno
        self.__accno=accno
        self.bal=bal
    @classmethod
    def display(cls):
        print(cls.bname,cls.__branch,cls.manager,cls.ifsc)
    def get_accno(self):
        print(self.__accno)
    @property
    def phno(self):
        print(self.__phno)
    @phno.setter
    def phno(self,new):
        self.__phno=new
        
c1=Bank('laxmi',987654233,234567890098765,9500000)
'''


'''       
>Bank.display()
SBI vijaynagar Ravi sbi012902
>c1.name
'laxmi'
>c1.phno
987654233
>c1.bal
9500000
>Bank.manager
'Ravi'
>Bank._Bank__branch
'vijaynagar'
>c1._Bank__accno
234567890098765
>c1._Bank__phno
987654233
>c1._name
'laxmi'
>c1.phno=234568090
>c1.phno
234568090
'''

#----------ABSTRACTION-------
'''
from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def check_bal():
        pass
    @abstractmethod
    def withdraw():
        pass
    @abstractmethod
    def deposit():
        pass
    @abstractmethod
    def update_pin():
        pass

class NewAtm(ATM):
    name='ICICI'
    loc='vijaynagar'
    def __init__ (self,name,accno,pin,bal):
        self.name=name
        self.accno=accno
        self.pin=pin
        self.bal=bal
    def check_bal(self):
        p=int(input("enter your atm pin:"))
        if p==self.pin:
            print('the available bal is:',self.bal)
        else:
            print('Invalid pin')
            

    def update_pin(self):
        p=int(input("enter your new pin:"))
        if p==self.pin:
            new=int(input('enter your new pin:'))
            self.pin=new
            print('pin updated successfully')
        else:
            print('Invalid pin')
            

    def deposit(self):
        p=int(input("enter your existing atm pin:"))
        if p==self.pin:
            amount=int(input('enter the amount to deposit:'))
            self.bal=self.bal+amount
            print('deposit successfully')
        else:
            print('Invalid pin')

    def withdraw(self):
        p=int(input("enter your existing atm pin:"))
        if p==self.pin:
            amount=int(input('enter the amount to withdraw:'))
            if self.bal>=amount:
                self.bal=self.bal-amount
            print('insufficient balance')
        else:
            print('Invalid pin')



c1=NewAtm('laxmi',23567890987654,1234,50000)

def operations(obj):
    print('enter 1 to check balance')
    print('enter 2 to update pin')
    print('enter 3 to withdraw')
    print('enter 4 to deposit')
    print('enter 5 to stop')
    while True:
        choice=int(input("enter your choice:"))
        if choice==1:
            obj.check_bal()
        elif choice==2:
            obj.update_pin()
        elif choice==3:
            obj.withdraw()
        elif choice==4:
            obj.deposit()
        elif choice==5:
            return 'thank you for using'
        else:
            print('invalid choice')

    
'''    
    

































