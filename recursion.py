#----recursion--> process of calling itself repeatedly until particular condition satisfied
'''
l=[1,2,[4,5,(9,8,{12,34,(9,11,17),35},12,18),19,89],66,1,5]
def sum_int(l):
    sum=0
    for i in l:
        if type(i)==int:
            sum+=i
        elif type(i) in [list,tuple,set]:
            sum+=sum_int(i)
    return sum
print(sum_int(l))
'''
'''
def reverse(s,rev='',i=0):
    if i>=len(s):
        return rev
    rev=s[i]+rev
    return reverse(s,rev,i=i+1)
print(reverse('good morning'))
'''
'''
def reverse(n,rev=0):
    if n<=0:
        return rev
    d=n%10
    rev=(rev*10)+d
    n=n//10
    return reverse(n,rev)
print(reverse(1234))
'''







