def fun(str1):
    print(str1)
    return
fun("I'm first call to user defined function!")
fun("Again second call to the same function")

def printme(str1,n):
    n[0]='Prasad'
    print(str1,n)
    return

x=['MP','Madhu']
printme("Wakeup",x)
print('x:',x)

def changeMe(lstn):
    lstn=['MP','PMS','Madhu']
    print(lstn)
    return
lst=[1,4,11,55]
print(changeMe(lst))
print('lst:',lst)
