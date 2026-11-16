#-----------------FILE HANDLING--------

#-------WRITE-------
'''
f= open ('file1.txt','w')
f.write('hello everyone\n')
f.writelines(['good afternoon\n','had your lunch\n','take care\n'])
f.close()
'''


#-----READ----------
'''
try:
    f=open('file1.txt','r')
    data= f.readlines()#(readlines-all the lines in the form of list)
    #data=f.read()#(read entire)
    #data=f.readline()#(readline-one line at a time)
except:
    print('file is not present')
else:
    print(data)
'''

'''
f=open('file1.txt','r')
f.write('ash loves anshh\n')
f.close()
'''

#-------w+(write&read)
'''
f=open('file1.txt','w+')
f.writelines(['today is monday\n','she loves him\n','he loves her\n'])
f.seek(9)
print(f.read())
print(f.tell())
f.close()
'''

#-------r+(read&write)
'''
f=open('file2.txt','r+')
f.seek(3)
f.write('he')
print(f.read())
f.close()
'''


'''
import pickle
data=[1,2,3,4,5]
c=pickle.dumps(data)
print(data,c)
f=open('file.txt','wb')
f.write(c)
f.close()
'''


'''
f=open('file1.txt','rb')
c=f.read()
print(c)
'''

#-CSV----(comma separated values)
'''
import csv

f=open('exam.csv','r')
obj=csv.reader(f)
for i in obj:
    print(i)

'''

'''

f=open('exam.csv','w',newline='')
ob=csv.writer(f)
ob.writerow(['Name','Contact','RollNo','Marks'])
ob.writerows([['Dora',9876543210,101, 90],['Smurf',98765456789,102, 80],['Chutki',9876541237,103, 85]])
f.close()
'''

import csv

f=open('exam.csv','a')
ob=csv.writer(f)
ob.writerow(['Dinku',9123443210,104, 95])



#context manager
with open('exam.csv','a') as f:
    ob=csv.writer(f)
    ob.writerow(['Bheema',9123478910,105, 75])
    
    




























