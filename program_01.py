Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from random import *
random()
0.09703482632675398
randint(10,20)
20
random()
0.44713027976292563
randint(10,20)
11
help(randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

help('randint')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    help('randint')
  File "<frozen _sitebuiltins>", line 103, in __call__
  File "C:\Program Files\Python311\Lib\pydoc.py", line 1993, in __call__
    self.help(request)
  File "C:\Program Files\Python311\Lib\pydoc.py", line 2049, in help
    elif request: doc(request, 'Help on %s:', output=self._output)
  File "C:\Program Files\Python311\Lib\pydoc.py", line 1777, in doc
    pager(render_doc(thing, title, forceload))
  File "C:\Program Files\Python311\Lib\pydoc.py", line 1751, in render_doc
    object, name = resolve(thing, forceload)
  File "C:\Program Files\Python311\Lib\pydoc.py", line 1737, in resolve
    raise ImportError('''\
ImportError: No Python documentation found for 'randint'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.
for i in range(100)
SyntaxError: expected ':'

=================================================== RESTART: Shell ==================================================
for i in range(100):
    print(randint(10,20),end=',')

    
Traceback (most recent call last):
  File "<pyshell#10>", line 2, in <module>
    print(randint(10,20),end=',')
NameError: name 'randint' is not defined

================================= RESTART: D:/Python_Practice31/Day18/program_03.py =================================
['D:/Python_Practice31/Day18/program_03.py']
Function name:D:/Python_Practice31/Day18/program_03.py

================================= RESTART: D:/Python_Practice31/Day18/program_04.py =================================
coming through stdout
hi mp

================================= RESTART: D:/Python_Practice31/Day18/program_05.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day18/program_05.py", line 2, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'

================================= RESTART: D:/Python_Practice31/Day18/program_05.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day18/program_05.py", line 2, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'

================================= RESTART: D:/Python_Practice31/Day18/program_05.py =================================
Sunday

================================= RESTART: D:/Python_Practice31/Day18/program_06.py =================================
<class 'datetime.datetime'>
-------------------------
2023-01-08 12:12:13.098794
2023
1
8
12
12
13
12:12:13
-------------------------
Traceback (most recent call last):
  File "D:/Python_Practice31/Day18/program_06.py", line 15, in <module>
    print("1 week ago it was:",ob-datetime.timedelta(week=1))
TypeError: 'week' is an invalid keyword argument for __new__()

================================= RESTART: D:/Python_Practice31/Day18/program_06.py =================================
<class 'datetime.datetime'>
-------------------------
2023-01-08 12:12:44.252776
2023
1
8
12
12
44
12:12:44
-------------------------
1 week ago it was: 2023-01-01 12:12:44.252776
100 days ago it was: 2022-09-30 12:12:44.252776
1 week from now it will be: 2023-01-15 12:12:44.252776
1000 days later it will be: 2023-04-18 12:12:44.252776
-------------------------
Birthday in... 8045 days, 12:12:44.252776
-------------------------

================================= RESTART: D:/Python_Practice31/Day18/program_06.py =================================
<class 'datetime.datetime'>
-------------------------
2023-01-08 12:14:26.725745
2023
1
8
12
14
26
12:14:26
-------------------------
1 week ago it was: 2023-01-01 12:14:26.725745
100 days ago it was: 2022-09-30 12:14:26.725745
1 week from now it will be: 2023-01-15 12:14:26.725745
1000 days later it will be: 2025-10-04 12:14:26.725745
-------------------------
Birthday in... 8045 days, 12:14:26.725745
-------------------------

================================= RESTART: D:/Python_Practice31/Day18/program_07.py =================================
Backup_8_1_2023_12_24_7.db

=================================================== RESTART: Shell ==================================================
from tkinter import*
root=Tk()
w=Label(root,text="Hello Learner!")
w.pack()
from tkinter import*
root=Tk()
w=Label(root,text="Hello Learner!")
w.pack()

=============== RESTART: D:/Python_Practice31/Day18/program_08.py ==============

=============== RESTART: D:/Python_Practice31/Day18/program_09.py ==============
Hello
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Hello
NameError: name 'Hello' is not defined

=============== RESTART: D:/Python_Practice31/Day18/program_09.py ==============

=============== RESTART: D:/Python_Practice31/Day18/program_09.py ==============
