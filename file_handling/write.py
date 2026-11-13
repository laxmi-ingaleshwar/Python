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
