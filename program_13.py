x=5;y=7
#Function definition is here
def changeme(mylist):
    p=89
    global x,y
    x=y+2
    mylist=[1,2,3,4]#This variable assign new reference in mylist
    print("values inside the function",mylist)
    print("local variables are:",locals())
    print("global variables are:",globals())
    return
#Now you can call changeme function
mylist_var=[10,20,30]
changeme(mylist_var)
print("values outside the function:",mylist_var)
