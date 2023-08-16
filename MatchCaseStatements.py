### Match in py is similar to switch case in java   ###
x=int(input("Enter the value of x: "))

match x:
    case 0:
        print("Value is 0")
    case 10:
        print("Value is 10")
    case _ if x<0:
        print(x,"is -ve Value")
    case _:
        print("Value is", x)                #Default statement