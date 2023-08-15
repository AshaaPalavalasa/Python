## String is an array of characters. Any text in double/Single quotes is considered as a string ##
name="Ashaa"
print("Names is "+name)
n=name[0]                   #can access individual characters of a string by indexing
namelen=len(name)
print(namelen)           #returns the length of the string starting with 0
## Looping through the Strings ##

for char in name:
    print(char)

## String Slicing ##                        #we can handle aa part of string using slicing
names="Ashaa,Swaroopa,Sai,Sushma"
print(names[6:14])                           # Indexing always starts with 0. And this indicated including 6 but not 14.
print(names[:5])
print(names[15:])
print(names[-6:])                         # Negative slicing starts from the end of the string and -ve indexing starts from -1.

## String Operations ##
## Strings are immutable. you can only create a copy and change it but cannot change the existing string ##
name="asHaa!!"
print(len(name))
print(name.upper())
print(name.lower())
print(name)                                 #Original string does not change and still prints "asHaa"
print(name.strip("!"))                      #Removes the tailing whitespaces or the tailing characters given.
print(name.replace("asHaa","Swaroopa"))     #Replaces the given character or string with the desired one.
print(name.split('H'))                     #Splits the string with the given separator and return a list
heading="my naMe is Ashaa"
print(heading.capitalize())                    #turns the 1st character in String to Upper Case and turns the rest of the String in lowercase
print(heading.center(60))                  
print(len(heading))
print(len(heading.center(60)))               #Aligns the string to the center as per alignment given by the user.This adds spaces/given characters to the string to increase the length by the alignement
print(name.center(50,"."))
print(name.count("a"))                  #Returns the number of times the given value occurred in the string
print(name.endswith("*"))               #Returns boolean if the string ends with the given value
print(name.endswith("a",2,5))           # we can even check if a apart of the string ends with the given value by using indexing
print(name.find("a"))                   # Returns the 1st occurance of the given value in a string,if not found returns -1.
# print(name.index("h"))                  #Returns exception if the given value is not found in the String
print(name.isalnum())                   #Returns true if the string only contains A-Z,a-z,0-9
print(name.isalpha())                    #Returns true if the string only contains A-Z,a-z
print(name.islower())                   #Returns true if the string is in lowercase
print(name.isprintable())               #Returns True if all the values in the string are printable. Ex: Use of sequence Characters in a string returns false.
print(heading.isspace())                # Returns TRue if the string contains only white space.
print(heading.istitle())                # Returns true if only if the 1st letter of each word is capital in a string
head="Hi, How Are You??"
print(head.istitle()) 
print(name.isupper())                   #Returns true if the string is in Uppercase
print(head.startswith("Hi"))            # Checks if the string starts with the given value
print(name.startswith("s",1,5)) 
print(name.swapcase())                  #Converts Uppercase to lowercase & lowercase to uppercase
print(heading.title())                  #Converts the string to titlecase i.e., capitalizes each letter of the word with in the string