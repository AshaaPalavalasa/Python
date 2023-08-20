###     Introduction to OOPs        ###
##      CLASS & OBJECT       ##
""" ---> Class is a blueprint or a template for creating a object. The user-defined objects are created using the class keyword"""
""" ---> Object is the instance of the class used to access the properties of the class."""
class Person:
    name="Ashaa"
    occupation="Software Tester"
    networth= 1
    def info(self):
        print(f"{self.name} is an {self.occupation}")
#       Self parameter is a referance to the current instance of the class and it is used to access variables that belong to the class       

a=Person()
a.name="Swaroopa"
a.occupation="Accountant"
# print(a.name,a.occupation,a.networth)
a.info()

###         CONSTRUCTORS            ###
##  ---> A constructor is a special method in class used to create and initialize an object of a class.
##  ---> There are different types of constructors.
##  ---> constructor is invoked automatically when an object of a class is created.
##  ---> The main purpose of a constructor is to initialize or assign values to the data members of that class.
##  ---> SYNTAX: "def __init__(self):"
##  ---> when a constructor accepts arguments, it is called 'Parameterized Constructor'
class Emp:
    def __init__(self,n,o):
        print("Hi!!")
        self.name=n
        self.occ=o
        print(f"I'm {self.name}, {self.occ}")

    def info(self):
        print(f"I'm {self.name}, and work as {self.occ}")

a=Emp("Ashaa","Developer")

##  ---> when a constructor does not accept any arguments and has only one argument that is self, it is called 'Default Constructor'

class details:
    def __init__(self):
        print("This is a Default Constructor")


###         Decorators          ###
##  ---> A Decorator is a function that takes another function as an argument and it modifies the behaviour of the original function.
##  ---> The new function is reffered as decorated function.
##  ---> Decorators are often used to add functionality, to functions and methods.
##  ---> SYNTAX: 
##      @decorator_function
##      def my_function:
##          pass

def greet(fx):
    def mfx(*args,**kwargs):
        print("Good Morning !!")
        fx(*args,**kwargs)
        print("Thanks for you visit !!")
    return mfx

@greet
def hello():
    print("Hello World")

def add(a,b):
    print (a+b)

hello()
greet(add)(1,2)

###      Getters & Setters       ###
##  ---> Getters in python are methods that are used to access the values of an object's properties.
##  ---> They are used to return value of a specific property, and are typically defined using @property deccorator.

##  ---> To set a value through we need setter method which can be added by decorating method with @property_name.setter
class Myclass:
    def __init__(self,val):
        self._val=val

    @property
    def value(self):
        return self._val

    @value.setter
    def value(self,new_val):
        self._val=new_val/10


obj=Myclass(10)
obj.value=1000
print(obj.value)