### TypeCasting is converting the datatype of a valid value to another --> throws an error if the value is not valid ###
a="1"
b="5"
print(a+b)                  # 15 but requried is 6
"""Explicit Typecasting: Conversion is done by the user"""
print(int(a)+int(b))        # 6         #str(),int(),float(),bool()..etc
"""Implicit TypeCasting: Python Converts smaller dataype to higher dataype automatically"""
c=10.5
d=10
print(c+d)                  # d is int, which is automatically converted into float