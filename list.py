Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,5,50,5.5,'hello',[100,200,'byebye',5.99,6j,'good'],[40,[1,9,'game'],599],'done']
len(l)
8
l[1]
5
l[4]
'hello'
l[5]
[100, 200, 'byebye', 5.99, 6j, 'good']
l[6]
[40, [1, 9, 'game'], 599]
>>> l[7]
'done'
>>> l[5][2]
'byebye'
>>> l[5][2][2]
'e'
>>> l[5][5][1]
'o'
>>> l[6][1][1]
9
>>> l[6][2][1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l[6][2][1]
TypeError: 'int' object is not subscriptable
>>> l[6][2]
599
>>> id(1)
140734619902888
>>> id(2)
140734619902920
>>> id(7)
140734619903080
>>> id(-1)
140734619902824
>>> l[2]



