Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=============================================== RESTART: D:/Python_Practice31/Day6/program_02.py ===============================================
Enter a value(o to end):5
Enter a value(o to end):3
Enter a value(o to end):11
Enter a value(o to end):0
Min: 3
Max: 11
avg: 6.333333333333333

=============================================== RESTART: D:/Python_Practice31/Day6/program_02.py ===============================================
Enter a value(o to end):5
Enter a value(o to end):3
Enter a value(o to end):11
Enter a value(o to end):0
Min: 3
Max: 11
avg: 6.3

=============================================== RESTART: D:/Python_Practice31/Day6/program_03.py ===============================================
Enter a value(-1 to end):4
Enter a value(-1 to end):5
Enter a value(-1 to end):3
Enter a value(-1 to end):4
Enter a value(-1 to end):8
Enter a value(-1 to end):7
Enter a value(-1 to end):0
Enter a value(-1 to end):1
Enter a value(-1 to end):-1
Even: 4 4 8 0
Min: 0
Max: 8
avg: 4.0
Odd:
Traceback (most recent call last):
  File "D:/Python_Practice31/Day6/program_03.py", line 18, in <module>
    print("Min:",min(lstOdd))
ValueError: min() arg is an empty sequence

=============================================== RESTART: D:/Python_Practice31/Day6/program_03.py ===============================================
Enter a value(-1 to end):4
Enter a value(-1 to end):5
Enter a value(-1 to end):3
Enter a value(-1 to end):7
Enter a value(-1 to end):8
Enter a value(-1 to end):0
Enter a value(-1 to end):1
Enter a value(-1 to end):-1
Even: 4 8 0
Min: 0
Max: 8
avg: 4.0
Odd: 5 3 7 1
Min: 1
Max: 7
avg: 4.0

=============================================== RESTART: D:\Python_Practice31\Day5\program_10.py ===============================================
Enter an integer ==> 4
4,00

=============================================== RESTART: D:\Python_Practice31\Day5\program_10.py ===============================================
Enter an integer ==> 45
45,44

=============================================== RESTART: D:\Python_Practice31\Day5\program_10.py ===============================================
Enter an integer ==> 84
84@,@8@8

=============================================== RESTART: D:\Python_Practice31\Day5\program_10.py ===============================================
Enter an integer ==> 84
84@,@8@4

=============================================== RESTART: D:\Python_Practice31\Day5\program_10.py ===============================================
Enter an integer ==> 54
54#,#5#4

=============================================== RESTART: D:/Python_Practice31/Day6/program_04.py ===============================================
one: 5
two: -18
3+4
7
print(3+4)
7
x=3+4
print(x)
7
print(x=3+4)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(x=3+4)
TypeError: 'x' is an invalid keyword argument for print()
print(x=3,4)
SyntaxError: positional argument follows keyword argument
import math
math.sqrt(2)
1.4142135623730951
math.gcd(24,40)
8
from math import *
sqrt(2)
1.4142135623730951
gcd(24,40)
8
from math import sqrt,gcd
sqrt(2)
1.4142135623730951
gcd(24,40)
8
import math as m
m.sqrt(3)
1.7320508075688772
m.sqrt(3)
1.7320508075688772
m.gcd(24,40)
8

================================================================ RESTART: Shell ================================================================
m.trunc(4.5)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    m.trunc(4.5)
NameError: name 'm' is not defined
import math as m
m.sqrt(3)
1.7320508075688772
m.god(24,40)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    m.god(24,40)
AttributeError: module 'math' has no attribute 'god'. Did you mean: 'gcd'?
m.gcd(24,40)
8
m.trunc(4.5)
4
m.floor(9.8)
9
m.ceil(9.1)
10
m.log(1024,2)
10.0
print('{0},{1},{2}'.format('apple','banana','carrot','pen'))
apple,banana,carrot
print('{0},{1} {0}{0}{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana appleapplepen carrot
print('{0},{1},{0},{0},{3} {2}'.format('apple','banana','carrot','pen'))
apple,banana,apple,apple,pen carrot
print('{0},{1},{0},{0},{3},{2}'.format('apple','banana','carrot','pen'))
apple,banana,apple,apple,pen,carrot

================================================================ RESTART: Shell ================================================================
print('{},{},{}'.format('apple','banana','carrot','pen'))
apple,banana,carrot
print('Jaanu purchased a kg of {},a dozen {},a kg of {}'.format('apple','banana','carrot','pen'))
Jaanu purchased a kg of apple,a dozen banana,a kg of carrot

================================================================ RESTART: Shell ================================================================
print('{2}, {1}, {0}'.format(*'abcd'))
c, b, a
x,*y,z='computer'
x
'c'
z
'r'
y
['o', 'm', 'p', 'u', 't', 'e']
*x,y='abcd'
x
['a', 'b', 'c']
y
'd'
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N' longitude='-115.81'))
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81'))
Coordinates: 37.24N, -115.81
print('WELCOME :{NAME}, YOUR COLLEGE IS: {COLLEGE IS: {COLLEGE}'.FORMAT(NAME='MP',COLLEGE='MTICA'))
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print('WELCOME :{NAME}, YOUR COLLEGE IS: {COLLEGE IS: {COLLEGE}'.FORMAT(NAME='MP',COLLEGE='MTICA'))
AttributeError: 'str' object has no attribute 'FORMAT'
print('WELCOME :{NAME}, YOUR COLLEGE IS: {COLLEGE IS: {COLLEGE}'.FORMAT(NAME='MP',COLLEGE='MTICA'))
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print('WELCOME :{NAME}, YOUR COLLEGE IS: {COLLEGE IS: {COLLEGE}'.FORMAT(NAME='MP',COLLEGE='MTICA'))
AttributeError: 'str' object has no attribute 'FORMAT'
