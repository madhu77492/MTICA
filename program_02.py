Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random as r
r.random()
0.8388761746386084
help(r.random)
Help on built-in function random:

random() method of random.Random instance
    random() -> x in the interval [0, 1).


================================ RESTART: Shell ================================
import random
random()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    random()
TypeError: 'module' object is not callable
random.random()
0.47537003725596905

================================ RESTART: Shell ================================
import random as r
r.random()
SyntaxError: multiple statements found while compiling a single statement

================================ RESTART: Shell ================================
import random as r
r.random()
0.7358522329962641
help(r.random)
Help on built-in function random:

random() method of random.Random instance
    random() -> x in the interval [0, 1).

r.randint(10,99)
40
help(r.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

help(r.uniform)
Help on method uniform in module random:

uniform(a, b) method of random.Random instance
    Get a random number in the range [a, b) or [a, b] depending on rounding.

r.uniform(10,100)
72.09739653647557
items=[1,2,3,4,5,6,7,8,9,10]
r.shuffle(items)
items
[4, 5, 8, 7, 3, 6, 10, 2, 9, 1]
a=[12,'papaya',45,7.8,'Mango']
r.shuffle(a)
a
['papaya', 7.8, 'Mango', 12, 45]
r.shuffle(a)
a
['papaya', 12, 7.8, 'Mango', 45]

=================================================== RESTART: Shell ==================================================
import random as r
items=[1,2,3,4,5,6,7,8,9,10]
x=r.sample(items,3)
x
[6, 7, 1]
x=r.sample(items,3)
x
[8, 5, 2]
x=r.sample(items,2)
x
[8, 2]

=================================================== RESTART: Shell ==================================================
from random import*
print(random())
0.650656144799269
print(randint(1,100))
84
print(uniform(1,20))
9.280278773137699
items=[1,2,3,4,5,6,7,8,9,10]
x=sample(items,3)
shuffle(items)
print(items)
[7, 10, 2, 9, 5, 3, 6, 8, 4, 1]
items=[1,2,3,4,5,6,7,8,9,10]
x=sample(items,3)
print("x=',x)
      
SyntaxError: unterminated string literal (detected at line 1)
items=[1,2,3,4,5,6,7,8,9,10]x=sample(items,3)
      
SyntaxError: invalid syntax
items=[1,2,3,4,5,6,7,8,9,10]
      
x=sample(items,3)
      
print("x=,x)
      
SyntaxError: unterminated string literal (detected at line 1)
items=[1,2,3,4,5,6,7,8,9,10]x=sample(items,3)
      
SyntaxError: invalid syntax

=================================================== RESTART: Shell ==================================================
from random import*
      
print(random())
      
0.23547139519120863
print(randint(1,100))
      
87
items=[1,2,3,4,5,6,7,8,9,10]
      
x=sample(items,3)
      
print("x=",x)
      
x= [8, 2, 4]
print(x[0])
      
8
y=sample(items,4)
      
print(y)
      
[6, 9, 5, 1]
