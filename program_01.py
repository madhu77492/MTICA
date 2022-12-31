Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dict1={'Name': 'MP','Age':'7','Class':'First'}
print(dict1)
{'Name': 'MP', 'Age': '7', 'Class': 'First'}
print(dict1['Name'])
MP
print(dict1['Age'])
7
print(dict1['Class'])
First
dict1['Course']='MCA'
print(dict1)
{'Name': 'MP', 'Age': '7', 'Class': 'First', 'Course': 'MCA'}
del dict1['Class']
print(dict1)
{'Name': 'MP', 'Age': '7', 'Course': 'MCA'}
dict1['Age']=6
print(dict1)
{'Name': 'MP', 'Age': 6, 'Course': 'MCA'}
del dict1[]
SyntaxError: invalid syntax
del dict1()
SyntaxError: cannot delete function call
dict1.clear()
print(dict1)
{}
dict1={'Name': 'MP','Age':'7','Class':'First'}
print(dict1)
{'Name': 'MP', 'Age': '7', 'Class': 'First'}
dict1.keys()
dict_keys(['Name', 'Age', 'Class'])
dict1.values()
dict_values(['MP', '7', 'First'])
dict1.items()
dict_items([('Name', 'MP'), ('Age', '7'), ('Class', 'First')])
for i in dict1:print(i)

Name
Age
Class
for i in dict1.keys():print(i)

Name
Age
Class
for i,j in dict1.items():print(i,j)

Name MP
Age 7
Class First

================================= RESTART: D:/Python_Practice31/Day10/program_02.py =================================
6
7
Traceback (most recent call last):
  File "D:/Python_Practice31/Day10/program_02.py", line 10, in <module>
    print(funAdd(inpNum1,inpNum2))
NameError: name 'inpNum2' is not defined. Did you mean: 'inpNUm2'?

================================= RESTART: D:/Python_Practice31/Day10/program_02.py =================================
7
6
13

================================= RESTART: D:/Python_Practice31/Day10/program_03.py =================================
I'm first csll to user defined function!
Again second call to the same function
Wakeup ['Prasad', 'Madhu']
x: ['Prasad', 'Madhu']

================================= RESTART: D:/Python_Practice31/Day10/program_03.py =================================
I'm first call to user defined function!
Again second call to the same function
Wakeup ['Prasad', 'Madhu']
x: ['Prasad', 'Madhu']

================================= RESTART: D:/Python_Practice31/Day10/program_03a.py ================================
I'm first call to user defined function!
Again second call to the same function
Wakeup ['Prasad', 'Madhu']
x: ['Prasad', 'Madhu']
['MP', 'PMS', 'Madhu']
None
lst: [1, 4, 11, 55]

================================= RESTART: D:/Python_Practice31/Day10/program_04.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day10/program_04.py", line 5, in <module>
    printDetail()
TypeError: printDetail() missing 2 required positional arguments: 'name' and 'marks'

================================= RESTART: D:/Python_Practice31/Day10/program_04.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day10/program_04.py", line 6, in <module>
    printDetail('MP')
TypeError: printDetail() missing 1 required positional argument: 'marks'

================================= RESTART: D:/Python_Practice31/Day10/program_04.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day10/program_04.py", line 6, in <module>
    printDetail('MP')
TypeError: printDetail() missing 1 required positional argument: 'marks'

================================= RESTART: D:/Python_Practice31/Day10/program_04.py =================================
Name 77
Marks: MP

================================= RESTART: D:/Python_Practice31/Day10/program_04.py =================================
Name MP
Marks: 77

================================= RESTART: D:/Python_Practice31/Day10/program_04.py =================================
Name MP
Marks: 77

================================= RESTART: D:/Python_Practice31/Day10/program_05.py =================================
Name MP
Marks: 77
Age: 22

================================= RESTART: D:/Python_Practice31/Day10/program_05.py =================================
Name 77
Marks: MP
Age: 22

================================= RESTART: D:/Python_Practice31/Day10/program_05.py =================================
Name MP
Marks: 77
Age: 22

================================= RESTART: D:/Python_Practice31/Day10/program_06.py =================================
add(): None
add(5): 5
add(5,7): 5
add(5,7,2): 5
add(5,7,2,11,55,77,22): 5

================================= RESTART: D:/Python_Practice31/Day10/program_07.py =================================
Enter string:day1
Enter string:day2
Enter string:day3
Enter string:day4
Enter string:day5
Written to file

================================= RESTART: D:/Python_Practice31/Day10/program_08.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day10/program_08.py", line 5, in <module>
    temp=fo1.read()
io.UnsupportedOperation: not readable

================================= RESTART: D:/Python_Practice31/Day10/program_08.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day10/program_08.py", line 5, in <module>
    temp=fo1.read()
io.UnsupportedOperation: not readable

================================= RESTART: D:/Python_Practice31/Day10/program_08.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day10/program_08.py", line 5, in <module>
    temp=fo1.read()
io.UnsupportedOperation: not readable

================================= RESTART: D:/Python_Practice31/Day10/program_08.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day10/program_08.py", line 4, in <module>
    temp=fo1.read()
io.UnsupportedOperation: not readable

================================= RESTART: D:/Python_Practice31/Day10/program_08.py =================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day10/program_08.py", line 4, in <module>
    temp=fo1.read()
io.UnsupportedOperation: not readable
