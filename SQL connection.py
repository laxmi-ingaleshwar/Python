import sqlite3
a=sqlite3.connect('data.db')
b=a.cursor()
#b.execute('create table Students(roll number, name varchar, phno number, marks number)')
'''b.execute("insert into Students values(101,'Dora',987654322,70)")
b.execute("insert into Students values(102,'Bheema',987654322,80)")
b.execute("insert into Students values(103,'Chutki',987654322,90)")
b.execute("insert into Students values(104,'Mr bean',987654322,99)")'''
data=b.execute('select * from Students')
# print(data.fetchone())          #(101, 'Dora', 987654322, 70)
# print(data.fetchone()[2])       # 987654322
# print(data.fetchmany(2))        #[(101, 'Dora', 987654322, 70), (102, 'Bheema', 987654322, 80)]
# print(data.fetchmany(3)[2])     # (103, 'Chutki', 987654322, 90)
# print(data.fetchmany(2)[1][1])  #Bheema
print(data.fetchall())            #[(101, 'Dora', 987654322, 70), (102, 'Bheema', 987654322, 80), (103, 'Chutki', 987654322, 90), (104, 'Mr bean', 987654322, 99)]
a.commit()
a.close()
