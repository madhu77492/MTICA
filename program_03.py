def Factorial(num):
    assert(isinstance(num,int)),"Factorial o defined for non integer !"
    assert(num>=0),"Factorial of negative number is not defined !"
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)
try:
    print(Factorial(-7))
except Exception as obj:
    print(obj)
try:
    print(Factorial(7))
except Exception as obj:
    print(obj)
try:
    print(Factorial(7.7))
except Exception as obj:
    print(obj)
try:
    print(Factorial('Madhu'))
except Exception as obj:
    print(obj)
