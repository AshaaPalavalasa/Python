###     SET     ###
##  ---> Collection of well-defined objects
##  ---> Unordeded
##  --->Immutable
##  --->Does not allow duplicates
##  ---> Seperated by comma & enclosed by {}

s={1,2,3,1,4,"Ashaa"}
print(s,type(s))                #  prints {'Ashaa', 2, 3, 4, 1} as duplicates are not allowed

## ---> To create a empty set
a=set()             
print(type(a))                  # prints set
b={}
print(type(b))                  # prints dict as the syntax of set & dict are same.They both are enclosed with {}

##  Accessing Set Items    ##
for value in s:
    print(value)



###         SET METHODS         ###
s1={1,2,3,4,5}
s2={4,6,7,8,9}

print(s1.union(s2))                 #returns a new set with all items in both the sets
print(s1,s2)
s1.update(s2)               ##adds items to the existing set
print(s1,s2)

c1={"Hyd","Che","Ban"}
c2={"Mum","del","kol","Ban"}
print(c1.intersection(c2))              # returns a new set which contains the elements present in both the sets
print(c1,c2)
c1.intersection_update(c2)              # modifies the set with the result
print(c1,c2)

n1={"Ashaa","Swaroopa","Sai"}
n2={"Sai","Sushma","Nanee"}
print(n1.symmetric_difference(n2))      # (A U B) - (A ^ B) ---> Return a new set
n1.symmetric_difference_update(n2)
print(n1,n2)                            # modifies the set with the result

alp1={"a","b","c"}
alp2={"b","f","g"}
print(alp1.difference(alp2))            # (A - B) ---> Returns new set
alp1.difference_update(alp2)
print(alp1,alp2)                        # modifies the set with the result

num1={1,2,3,4}
num2={4,5,6,1}
print(num1.isdisjoint(num2))            # (A ^ B)=0. Checks if elements of given set are present in another set. Returns FALSE if PRESENT
print(num1.issuperset(num2))            #(A ^ B)=B. Returns true if all elemnts of B are present in A.
print(num2.issuperset(num1))            #(A ^ B)=A. Returns true if all elemnts of A are present in B.

a.add(3)
print(a)                    #adds a element into the set 
c=("ashaa",5,"hi")
a.update(c)             # adds more than 1 elemnt to the set
print(a)

 # removes the item from the set.
a.remove(3)
print(a)                # When you use remove() for a elemnt which is not present in list..ERROR popups.
a.discard("hi")
print(a)                # When you use discard() for a elemnt which is not present in list..ERROR doesnot raise.

a.pop()         # This method removes the last element of the set, but we cant be sure which elemnt gets removed as sets are unordered.
print(a)

del a               # deletes the entire set
# print(a)            #Error  popsup as the entire set is deleted

print(num1)
num1.clear()        # clears the set element and makes it empty
print(num1)

##      Check elemnt in set     ##
if 4 in num2:
    print("Present")
else:
    print("You lost it")