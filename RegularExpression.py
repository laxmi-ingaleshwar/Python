#---------Regular Expression

data= '''employee mail 4455773445 id is pallavi@gmail.com
        9876543210 TYP2697 Yashwanth123@gmail.com 234567
        PENT456 ashwini.k@pqr.in  9988776655 12-09-2026 '''


'''
pattern = r'[6-9]\d{9}'
import re
phno = re.findall(pattern,data)
print(phno)
'''
#output:['9876543210', '9988776655']


'''
pattern = r'[A-Z]{3,5}\d+'
import re
empid =re.findall (pattern,data)
print(empid)
'''
#OUTPUT: ['9876543210', '9988776655']


'''
pattern = r'\d{2}[./-]+\d{2}[./-]+\d{2,4}'
import re
date = re.findall(pattern,data)
print (date)
'''
#OUTPUT: ['12-09-2026']


'''
pattern = r'[a-z]+.?\d*[a-z]*\@[a-z]+.[a-z]{2,3}'
import re
email = re.findall(pattern,data)
print (email)
'''
#OUTPUT: ['is pallavi@gmail.com', 'ashwanth123@gmail.com', 'ashwini.k@pqr.in']














