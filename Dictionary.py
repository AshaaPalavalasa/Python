##      Dictionary      ##
##  ---> Ordered after 3.7 version
##  ---> Combination of Key:Value pairs
##  ---> Seperated by comma & enclosed by {}
##  ---> Mutable

thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
print(thisdict)
print(thisdict["year"])                 # Returns error if the key is not present in dict
print(thisdict.get('model'))            # Returns None if the key is not present in dict


## Accessing multiple values

print(thisdict.values())                # Returns all the dict values 
print(thisdict.keys())                  # Returns all the dict keys 

for key in thisdict.keys():
    print(f"The value corresponding to {key} is {thisdict[key]}")                # Prints Values according to the keys

print(thisdict.items())
for key,value in thisdict.items():
    print(f"The value corresponding to {key} is {value}")                # Prints Values according to the keys

ep1={'emp1':45,'emp10':89,'emp4':69,'emp5':69}
ep2={'emp2':88,'emp4':76,'emp3':90}

ep1.update(ep2)                # updates the value of the key provided to it if the item exists in the dict or creates a new value pair
print(ep1)

ep1.clear()                    # Removes all the items from the dictionary
print(ep1)

ep1={'emp1':45,'emp10':89,'emp4':69,'emp5':69}
ep1.pop('emp4')                # Removes the key-value pair whose key is passed as argument
print(ep1) 

ep1.popitem()                   # Removes the last key-value pair in dict
print(ep1)

del ep1                         # Deletes the complete dict
# print(ep1)                      # Throws error "name 'ep1' is not defined" as dict is deleted

ep1={'emp1':45,'emp10':89,'emp4':69,'emp5':69}
del ep1['emp1']                 # Deletes the key value pair if key is specified
print(ep1)

