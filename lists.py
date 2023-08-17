##      Lists       ##
##  --> Lists are ordered collection of datatypes.
##  -->They store multiple varibales under a asingle variable
##  -->Lists are enclosed by [] & are changable after creation

marks=[3,4,5,6,"Harry",True]
print(marks)
print(type(marks))
print(marks[0])         #Elements of the list are accessed by indexing starting with zero
print(marks[1:-2])
print(marks[::2])          # Jump Index works with lists also.

if "Harry" in marks:    # Verifying elemnts are present in the list. 
    print("Present")
else:
    print("Not Present")

if "6" in marks:            #integers cannot be identifed if passed as string
    print("present")
else:
    print("Not present")

###         List Comprehesion       ###
##  --->List Comprehension are used to create new lists from other iteratables.
##  --->Syntax: list=[Expression(item) for item in iterable if Condition]

lst=[i*i for i in range(5)]
print(lst)
lst2=[i for i in range (10) if i%2==0]
print(lst2)

###     List Methods     ###

l=[1,12,3,1,24,5,10]
l.append(10)            # adds element at the end
print(l)
l.sort()                # sorts the list in ascending order..
print(l)
l.sort(reverse=True)    # for desecding order (reverse=True)
print(l)
l.reverse()             # reverses the list
print(l)
print(l.index(10))       # returns the 1st occurance index of the element in the list
print(l.count(1))        # returns the count of the occurance of the given item in the list
l2=l.copy()              # Returns the copy of list
l2.insert(1,999)         # Inserts the item at the given index.
print(l2)
l3=["hi",7,'@']          # Appends a list at the end of another
l2.extend(l3)
print(l2)
print(l+l3)             # Adding 2 lists can also be done without changing the original lists