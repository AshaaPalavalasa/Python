###     Tuples      ###
##  --->Tuples are ordered collecton of data type.
##  --->Tuples are enclosed by ()
##  ---Tuple elements are seperated by comma, even if only one element is present for the complier to identify it as tuple.
##  ---> Tuples are immutable once created.

tup=(1,)
print(tup,type(tup))
# tup[0]=2            ## ERROR: tuple' object does not support item assignment
tup=(2,3,45,7)
print(tup[0])
print(tup[-2])
print(tup[::2])

## Check for Element
if 3 in tup:
    print("Present")

##  Tuple Methods   ##
##  --->Tuples are immutable, hence if we wnat to add,remove or change tuple items, then first you can connect the tuple to a list.

tup1=("India","America","Sweden","London","America")
tup2=("Australia","Austria","Singapore")

print(tup1.count("America"))
print(tup1+tup2)
print(tup1.index("America"))        ## Raises value error if element is not available
print(tup1.index("America",2,len(tup1)))            ## Verifies within the given start and end range
