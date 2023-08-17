##      Exception Handling is process of responding to unwanted or unexcepeted events when a program runs       
##      Try-Except blocks are used to handle the exceptions.
##      The code in try block runs when there is no error.
##      If try block catches a error, except block is executed


a=input("Enter a num: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
    print("THE END")
except:
    print("Code which has to be executed when a error occurs")

##  Multiple except can be used for a single string based on the error

try:
    num=int(input("Enter a num: "))
    a=[1,2,3,4,5]
    print(a[num])
except ValueError:
    print("Entered value is not a number")
except IndexError:
    print("Index does not exists")


###         Finally Clause          ###
##      Finally block is always executed irrespective of the error status
##      In general the function ends at return statement, if we want to execute some code after the return finally is used.

def func():
    try:
        l=[1,2,3,4,5,6,7,8,9]
        i=int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Error Occured")
        return 0
    finally:
        print("Finally block is always executed!!")

x=func()
print(x)

