# Variable is like a container which holds data #
""" A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive"""
a=1                         # int
b="harry"                   # string
c=True                      # Bool
print(a, b, c)

# DataType specifies the value a variable holds #
# print(a+b)                                #ERROR: unsupported operand type(s) for +: 'int' and 'str'
print("The type of a is:",type(a))         # Gives the datatype of the data stored in the variable   
print("The type of a is:",type(b))
print("The type of a is:",type(c))

###  Build In Data Types  ###
# 1. Numeric Data: Int, Float, Complex
d=4
e=5.7
f=complex(6,2)

print(d, type(d))           #int
print(e, type(e))           #str
print(f, type(f))           #complex

# 2. Text Data: Str
g="Hello!!"

print(g, type(g))           #str

# 3. Boolean Data--> Boolean data contains of only 2 values-->Either True/False
h=True
print(h,type(h))            #bool

# 4. Sequence Data: List, Tuple
''' List: List is a ordered collection of data which are comma seperated and enclosed by square brackets.
-->Lists are "Mutable" i.e., can be modified after creation'''
i=[1,2.987,"Ashaa",["ab","bc",1]]

print(i,type(i))            #list

'''Tuple: Tuple is a ordered collection of data which are comma seperated and enclosed by parenthesis
--> Tuples are "Immutable" i.e., cannot be modified after creation'''
j=(1,2.9578,"Swarropa",('Hi','Hello','Namaskaram'))

print(j,type(j))           #tuple

# 5.Mapped Data: dict
'''Dict: Dict is an unordered collection of data with kry:value pairs and are enclosed by square brackets'''
k={'Telugu':"Namaskaram",'English':"Hi!!",'Kannada':"Namaskara"}

print(k,type(k))           #dict


