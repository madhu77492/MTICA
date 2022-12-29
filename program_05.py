def div(a,b):
    assert( isinstance(a,int) or isinstance(a,float)), \
              'First Argument should be either Integer or float'
    assert( isinstance(b,int) or isinstance(b,float)), \
              'Second Argument should be either Integer or float'
    assert(b!=0),"Division by zero is not defined !"
    return a/b
    
try:
    print(div(7,0))
except AssertionError as obj:
    print(obj)
try:
    print(div(7,6))
except AssertionError as obj:
    print(obj)
try:
    print(div(7,2))
except AssertionError as obj:
    print(obj)
