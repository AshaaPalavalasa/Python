###     Map, Filter & Reduce        ###
'''    ---> these are built-in functions which allows you to apply a function to a sequence of elemnets and return a new sequence.
       ---> They are called higher-order functions, as they take other functions as arguments'''

##      MAPS        ##
'''  --->    Map func applies a function to each elemnt in a sequence and return a new sequence containing the transformed elements.
     ---> SYNTAX: "map(function,iterable)" '''

##  ---> Requirement is to get the cubes of the list of elemnts. Generally we follow loops.

# def cube(x):
#     return x**3

l=[1,2,3,4,5]
# reslist=[]
# for i in l:
#     reslist.append(cube(i))

# print (reslist)

## ---> Instead of using this loop, we can use a map function

# reslist=list(map(cube,l))
reslist=list(map(lambda x:x**3,l))      
print(reslist)

###      FILTER      ###
'''  ---> Filterfun filters a sequence based on a given predicate() fun that returns a boolean value and returns a new sequence that containing only the elements that meet thr predicate.
     ---> SYNTAX: "filter(predicate,iterable)" '''

# def filter_fun(a):
#     return a>=3
# newlist=list(filter(filter_fun,l))

newlist=list(filter(lambda x: x>=3,l))
print(newlist)


###         REDUCE          ###
'''     ---> Reduce is a higher-order function that applies a fun to a sequence and return a single value
        ---> It is a part of functools module in python and hence has to be imported before using. 
        SYNTAX: "reduce(function,iterable)" '''

from functools import reduce

sum=reduce(lambda x,y:x+y,l)
##  --> the function takes 2 values and return a single value
print(sum)          # l=[1,2,3,4,5] so 1+2+3+4+5=15
