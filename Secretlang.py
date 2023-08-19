# Write a program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove 1st letter and append it to the end
# now append 3 random characters at the starting and the end
# else
# reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else
# remove 3 random characters from start and end.Now remove the last letter and append it at the beginning
# ur program should ask whether to code or decode

import random
import string

def givetheDecodedstring(str): 
    strlen=len(str)
    ansstr=""
    if(strlen>=3):
        newstr=""
        for i,char in enumerate(str):
            if(i>2 and i<strlen-3):
                newstr+=char
        ansstr=newstr[-1]
        orglen=len(newstr)
        for i in range(orglen-1):
            ansstr+=newstr[i]    
    else:
        for i in range(strlen):
            ansstr+=str[strlen-i-1]
    return ansstr


def givetheencodedstring(str):
    strlen=len(str)
    ansstr=""
    if(strlen>=3):
        newstr=""
        for index,char in enumerate (str):
            if index==0:
                continue
            else:
                newstr+=char
        newstr+=str[0]      
        for i in range(7):
            if i==3:
                ansstr+=newstr
            else:
                ansstr+=random.choice(string.ascii_letters)
    else:
        for i in range(strlen):
            ansstr+=str[strlen-i-1]
    return ansstr




type=input("Enter decode/encode: ")
string1=input("Enter the String to process: ")
if (type=="encode"):
    print(givetheencodedstring(string1))
elif type=="decode":
    print(givetheDecodedstring(string1))

        
        


            

