def div(a,b):
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
