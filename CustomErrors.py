###     In python we can raise a error by using Custom Errors


a= int(input("Enter any value between 5 & 10: "))
if(a<5 or a>10):
    raise ValueError("Value is not between the desired limit")

##  In python we can create a new custom error by defining a class.