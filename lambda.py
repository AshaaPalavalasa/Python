###         Lambda function          ###
##  --->    small function without name.
##  --->    often used in situations where a small single expression function is required in a short period of time
##  --->    SYNTAX: "lambda arguments: expression"

# def double(val):
#     return val*2

## The above function can also be written as

def apply(fx,val):                  # Calling a fun inside a fun
    return 6+fx(val)

double=lambda x:x*2
cube= lambda x:x*x*x
avg= lambda x,y,z: int((x+y+z)/3)
mult= lambda x,y:print(f'{x} X {y} = {x*y}')

print(double(5))
print(cube(5))
print(avg(3,5,10))
mult(2,3)

print(apply(lambda x:x*2,2))        # lambda funcs are commonly used as arguments to higher-order functions