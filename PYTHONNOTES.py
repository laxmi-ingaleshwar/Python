#PYTHON
python is a programming language, Which is used to interact with the machines/ computer.

#Types.
1.Low level Language.
2.Middle level Language.
3.High level Language.

#1.Low level Language-
which consists of binary values such as 0s & 1s, Machines can easily understnad.
#2.Middle level Language-
which consists of mnemonics& it uses a device called assembler to convert
mnemonics to binary.
#3.High level Language
Language is a programming language which humans can understand easily.
It uses translator to convert High level language to binary language.
#ex-- Python, Java,C++

#Translator--
Device which are used to convert high level language to low level language& vice versa.

#Types of translators.
#1. Compiler
It executes complete code at a time & it raises all the errors at last if present.

#2. Interpreter
It executes code line by line if there is an error in the particular line until & unless we clear it,
it will not goto the next instructions so, that it makes debugging easier.

Python is a general purpose, high level, dynamically typed programming language.
Which was developed by GUIDO VAN ROSSUM in 1991.

#FEATURES.
1. Easy to learn & analyse.
2. High level Language.
3. Interpreted language
4. Open source
5. Dynamically Typed Language
6. Platform Independent.
7. Multi paradigm.
8. Huge library functions
9. Huge community support
10. Multi purpose.

#KEYWORDS
Keywords are Universal Standard words, which are pre-defined by the developer.
We can access their functionalities but we cannot modify their Original Task.

These are 35 keywords in python.
syntax
import keyword
keyword.kwlist

True=1,False=0,None=absence of value, considered as Special Keywords.
As they contain some internal values & we can assign these keywords as value to variable.

#VARIABLE
Variable is like container used to store value.

#IDENTIFIERS
identifiers are the meaningful names given to the user-defined entities such as
Variables,functions,classes & objects.

#RULES
1.should not be a keyword
2.should not contain special characters as except underscore
3.it should not start with numbers
4.it can be alphabet,group of alphabets,alphanumeric

#DATATYPES
datatypes are used to specify the size & type of the value.

TYPES
#I.Single value Datatypes
#1.Integer(int)
* It is a whole number without fractional / decimal point
* It can be both +ve & -ve
* Default value of Integer is 0, which can be access using int().


#2.Float
* The real Numbers with decimal point considered value
* The float is 0.0 which can be accessed using float().
* It is mandatory to mention atleast one digit along with the decimal point.
* After decimal point it takes upto 16 digits, but not more than that.



#3.Complex
* It is a combination of real & Imaginary part.
* a +- bj
* Apart from j we cannot use any other character as imaginary value.



#4.Boolean(bool)
* Boolean is a smallest datatype which contains only two values such as true/false.
* False is a default value & True is the non-default value.
* These values can be used as result and while checking some conditions.



#II.Multi value Datatypes
#1.String
* String is a collection of characters, which is enclosed between
''(single quote), ""(double quote), ''' '''(triple quote).
* A string can contain alphabets,digits & special characters.
* Default value of string ''.

#2.List[]
* List is a collection of Hmogeneous/ Heterogeneous type of values,
* which is enclosed between [].
* The default value of list is [].
* List is a order collection which supports indexing.
* List allows duplicate values.
* List is a mutable datatype.
* Syntax  Var=[V1,V2,----,Vn]
#functions to add the value to the list.
1.append()
    * add one element to the end of the array.
    * list.append(val)
2.insert()
    * add an element at the specific index at a list.
    * list.insert(index,value)
3.extend()
    * add multiple elements to the end of the list.
    * list.extend([V1,V2,-----,Vn])

#3.Tuple()
* Tuple is an ordered collection which supports indexing.
* It is a immutable datatype.
* The default value of tuple is ().
* which can be accessed using tuple().
* Storing a single value inside is not possible directly,
* It should be stored with (,)comma.


#4.Set{}
* Set is a collection of homogeneous & Heterogeneous type of value,
* Which are enclosed between {}.
* Set is a mutable value.
* It is an unordered collection that does not supports indexing.
* Set does not allow duplicate values.
* We cannot store mutable values inside set.
* The default value of set is Set().

#FUNCTIONS TO ADD THE VALUES TO THE SET.
1.add()
* Used to add an element randomly to the set.
* Set.add(val)

2.Update()
* Add multiple values at a time to the random positions of set.
* Set.update(collection)
* Set.update(collection1,collection2,....)


#FUNCTIONS TO REMOVE THE VALUES TO THE SET.
1.pop()
* Removes first element from the set.
* Set.pop()

2.remove()
* Remove the specific value.
* Set.remove(val)


#5.Dictionary{}
* It is a collection of key & value pairs, enclosed between {}.
* #Syntax= {K1:V1, K2:V2, K3:V3,.........,Kn:Vn}.
* Dictionary is mutable.
* Key must be unique & immutable.
* Values can be anything.
* Default value of dictionary is {}.
* # Ex= {'a':'apple', 'b':'banana', 'c':'carrot'}
* Dictionary doesnot support indexing but using keys we can access the value.

#DICTIONARY LOOK UP METHOD.
* The process of accessing value using keys.
* Syntax:  Var(key)
* Dictionary is mutable datatype.
* We can add key value pair & modify the existing values using  Var(key)=value

#FUNCTION TO REMOVE KEY-VALUE PAIRS.
1.pop()
* it will remove the value from the dictionary based on the mentioned key.
* Syntax= dict.pop(key)
*       / dict.pop(key,arg)
* #If key is not present it returns arguments.

2.popitem()
* used to remove the last key value pair.
* Syntax= dict.popitem()



#SLICING
* Slicing is a process of extracting multiple values from a collection in a sequential order.
* syntax=  var[SI:EI:STEP]
* slicing is completely depending on indexing.
* It supports only the collection on which we can perform indexing.[string,list,tuple].



#COPY OPERATION
* process of copying the content from one variable to another variable.
1.General / Reference copy.
2.Shallow copy.
3.Deep copy.


#1.Reference copy.
* Process of assigning one variable to the another &
* both the variables point to the same object in memory.
* If the values() are mutable datatype,
* modification done on one variable will affect another variable also.
* #syntax= destination_variable = source_variable


#2.Shallow copy.
* It creates new outer object but the Nested objects are still shared.
* #syntax = import copy
* #         destination_variable = copy.copy(source_variable)          


#3.Deep copy.
* It creates completely an independent copy including Nested mutable values.
* #syntax=  import copy
* #         destination_variable = copy.deep copy(source_variable)


#TYPE CASTING
* Type casting is the process of converting one type of data into another type.
*# syntax= destination_type(data)/
#          data_type(data)


#OPERATORS
* Operators are the special symbols which are used to perform a specific task.
*# TYPES OF OPERATORS
* 1. Arithmetic Operator
* 2. Relational Operator
* 3. Logical Operator
* 4. Bitwise Operator
* 5. Assignment Operator
* 6. Membership Operator
* 7. Identify Operator


# 1. Arithmetic Operators
* These are used to perform basic mathematical operations.
* 1.Addition(+)
* 2.Subtraction(-)
* 3.Multiplication(*)
* 4.Division
    i.true(/)
    ii.floor(//)
    iii.modulus(%)
* 5.Exponent/power(**)


# 2.Relational/ comparison Operator.
* These are used to compare two values & the result will be always true.
* 1.Relational equal to(==)
* 2.Relational not equal to(!=)
* 3.Relational greater than(>)
* 4.Relational lesser than(<)
* 5.Relational greater than equal to (<=)
* 6.Relational lesser than equal to (<=)

# 3.Logical Operators.
* It is used to combine multiple conditions.
* 1.Logical AND
* 2.Logical OR
* 3.Logical NOT











