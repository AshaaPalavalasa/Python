                            ## If-Else Statement ##

a=input("Enter your age: ")
a=int(a)

if(a>=18):
    print("You can vote")
else:
    print("You can't vote")
print("Have a Good Day!!!")

                            ## Elif Statement ##

num=int(input("Enter a val: "))
if(num>0):
    print("Number is +ve")
elif(num<0):
    print("Number is -ve")
elif(num==0):
    print("You have given Zero !!!")
else:
    print("Please Enter a Number !!!")

                            ##  Nested if Statement ##

num=int(input("Enter a val: "))
if(num>0):
    print("Number is +ve")
    if(num>9):
        print("Your Number is 2 digit number")
    else:
        print("You Number is Single digit number")
elif(num<0):
    print("Number is -ve")
elif(num==0):
    print("You have given Zero !!!")
else:
    print("Please Enter a Number !!!")

