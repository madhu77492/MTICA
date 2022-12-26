Python 3.11.0a5 (main, Feb  3 2022, 19:32:53) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=============================================== RESTART: D:/Python_Practice31/Day5/program_01.py ===============================================
256
-8

=============================================== RESTART: D:/Python_Practice31/Day5/program_02.py ===============================================
Hello world
Value of x is 8 value of y is 10

=============================================== RESTART: D:/Python_Practice31/Day5/program_03.py ===============================================
s1
'This\nis a multi-line\nstring.'
print(s1)
This
is a multi-line
string.

=============================================== RESTART: D:/Python_Practice31/Day5/program_04.py ===============================================
Traceback (most recent call last):
  File "D:/Python_Practice31/Day5/program_04.py", line 3, in <module>
    print("s0:",so)
NameError: name 'so' is not defined. Did you mean: 's0'?

=============================================== RESTART: D:/Python_Practice31/Day5/program_04.py ===============================================
s0: *	*
**	**
**	***

s1: I said,"This is a valid string."

=============================================== RESTART: D:/Python_Practice31/Day5/program_04.py ===============================================
s0: *	*
**	**
***	***

s1: I said,"This is a valid string."

=============================================== RESTART: D:/Python_Practice31/Day5/program_04.py ===============================================
s0:
 *	*
**	**
***	***

s1:
 I said,"This is a valid string."

=============================================== RESTART: D:/Python_Practice31/Day5/program_06.py ===============================================
Cats	are
	good	sources
		opf	internet	memes
s
'Cats\tare\n\tgood\tsources\n\t\topf\tinternet\tmemes'

=============================================== RESTART: D:/Python_Practice31/Day5/program_06.py ===============================================
Cats	are
	good	sources
		of	internet	memes
s
'Cats\tare\n\tgood\tsources\n\t\tof\tinternet\tmemes'

=============================================== RESTART: D:/Python_Practice31/Day5/program_07.py ===============================================
\\\\
\
\
\

Good-bye
'abc' 'def'
'abcdef'
'abc' + 'def'
'abcdef'
x= 'abc'
y= 'def'
x+y
'abcdef'
x y
SyntaxError: invalid syntax
x.y
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x.y
AttributeError: 'str' object has no attribute 'y'
x*y
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x*y
TypeError: can't multiply sequence by non-int of type 'str'
xy
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    xy
NameError: name 'xy' is not defined. Did you mean: 'x'?
s1= 'abc'*4
s1
'abcabcabcabc'
s2= 'abc'*4
print(s2)
abcabcabcabc
