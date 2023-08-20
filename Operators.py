# 1.Arithmetic Operators
""" +   --->    Addition
    -   --->    Subtraction
    *   --->    Multiplication
    /   --->    Division
    %   --->    Modulus
    **  --->    Exponential
    //  --->    Floor Division """

a=5
b=2
c=[1,2]
d=[1,2]

print(a+b)          #7
print(a-b)          #3
print(a*b)          #10
print(a**b)         #25
print(a%b)          #1
print(a/b)          #2.5
print(a//b)         #2--> divides the values and gives only the interger value and omits the decimal value

# 2. Comparition  Operators
''' >   --->    Greater Than
    <   --->    Less Than
    >=  --->    Greater Than or Equals To
    <=  --->    Less than or equals to
    ==  --->    Compares the values of the object
    is  --->    Compares the location of the object'''

print(a>b)          #True
print(a<b)          #False
print(a>=b)         #True
print(a<=b)         #False
print(a==b)         #False
print(d==c)         #True
print(d is c)       #False  
'''---> IS returns True if the values are given some constant value or None, 
    as python doesnot create multiple constant values at different location with same value'''
d=3
c=3
print(d==c)         # TRUE
print(d is c)       # TRUE because after creating a constant as it cannot be changed, python directs the next varaiable with same value to the same memory.

