##  Functions       ---> Block of code that performs a specific task when called.
###     Built-In & User-Defined Functions     ###
##      Userd-defined   --->    functions created by the user to perform specific tasks
##      Built-In        --->    functions which are pre-coded in python

def calculategmean(a,b):
    maxNum(a,b)
    mean=(a*b)/(a+b)
    print(mean)

def maxNum(a,b):
    print(max(a,b),"is greater")            # max,print are a built-in function

calculategmean(2,3)
calculategmean(4,5)
calculategmean(8,7)

##  Passing Function Arguments  ##
###     There are 4 types of Arguments     ###
#   ---> Default Arguments
#   ---> Keyword Arguments
#   ---> Variable Length Arguments
#   ---> Required Arguments

def ave(a=9,b=10):              #---> Default Arguments: assumes a default value even if a value is not provided in the function call
    print("the avg is",(a+b)/2)

ave(3)      #a=3,b=10
ave()       #a=9,b=10
ave(b=9)    #a=9,b=9

def name(fname,mname,lname):     #---> Keyword Arguments: The arguments are passed as key=value pair while calling. so the order in which parameters are passed does not matter
    print("Hi @",fname+" "+mname+" "+lname)

name(mname='',fname='Ashaa',lname='Palavalasa')
name(lname='Palavalasa',fname='Swaroopa',mname='')

''' Required Arguments: If we don't pass the arguments with a key=value syntax,then it is necessary to pass the arguments in correct 
    positional order and the number of arguments should match with function definition'''

name("Ashaa","","Palavalasa")

### Variable-Length Arguments: Sometimes we need to pass more arguments then that are defined in the function. This can be done by Variable-length arguments
def average(*numbers):  
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average",sum/(len(numbers)))

average(1,2,3,4,5)
average(2,2)
average(5,6,7)

def myname(**name):             ##  Passing arguments as dict
    str="Hello!"+name["fname"]+name["lname"]
    return      str

fullname=myname(fname="Ashaa",lname="Palavalasa")
print(fullname)