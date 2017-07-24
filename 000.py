Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=b
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=b
NameError: name 'b' is not defined
>>> A = B
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    A = B
NameError: name 'B' is not defined
>>> (a=b)
SyntaxError: invalid syntax
>>> a = 5
>>> b = 10
>>> a = 10
>>> a = b
>>> b = a
>>> a=5
>>> b=10
>>> a
5
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> b
10
>>> c=a
>>> a=b
>>> b=c
>>> a
10
>>> b
10
>>> a=5
>>> b=10
>>> a
5
>>> c=a
>>> a=b
>>> b=c
>>> c
5
>>> b
5
>>> a
10
>>> four='4'
>>> print(four*3)
444
>>> five=4
>>> print(five)
4
>>> print(five*3)
12
>>> print('my name is '+'my name)
      
SyntaxError: EOL while scanning string literal
>>> print("my name is " + my name)
SyntaxError: invalid syntax
>>> my_name = ‘student’'
>>>hi+my name
SyntaxError: invalid character in identifier
>>> 
>>> print ('hi,+my name')
hi,+my name
>>> print('I am '+my_age+'years)
      
SyntaxError: EOL while scanning string literal
>>> print('I am '+my_age+'years old')\

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print('I am '+my_age+'years old')\
NameError: name 'my_age' is not defined
>>> print('I am '+my_age+'years old')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print('I am '+my_age+'years old')
NameError: name 'my_age' is not defined
>>> print("I am"+my_age+"years old")
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print("I am"+my_age+"years old")
NameError: name 'my_age' is not defined
>>> print('I am '+'my_age'+'years old')
I am my_ageyears old
>>> print('I am '+'15'+'years old')
I am 15years old
>>> total=('score'+'count*2)
       
SyntaxError: EOL while scanning string literal
>>> pprint('total')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    pprint('total')
NameError: name 'pprint' is not defined
>>> print(;total')
      
SyntaxError: invalid syntax
>>> print('total')
total
>>> 
