#Raise an error and stop the program if x is lower than 0:
#x=-1
x=int(input())

if x<0:
    raise Exception("Sorry,no number below zero")
