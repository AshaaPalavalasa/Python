###     Handles a file

f=open('textfile.txt')              # Opens the file in read mode by default
text=f.read()                       # reads the file
print(text)
f.close()                           # Closes the oped file

## Write in a file

f=open('textfile.txt','w')          # Opens the file in write mode
f.write('you can edit it ')          # Overwrites the text in the file
f.close()

f=open('textfile.txt','a')          # opens the file in append mode
f.write('according to your requirement ')
f.close()

##  You can use the with statement to automatically close the file after you are done 

with open('textfile.txt','a') as f:
    f.write("this file is needed")

###     readline()  --> reads a single line from the file. if we want to read multiple lines, we can use a loop.
f=open('textfile.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)

###     writelines()    ---> writes a sequence of strings to a file.

f=open('textfile.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()

###     seek()      ---> allows you to move current position within a file to specific point. The position is specified in bytes.
with open('textfile.txt','r') as f:
    f.seek(10)              # Move to 10th byte in the file
    data=f.read(5)          # Reads the next 5 bytes
    print(data)

###     tell()          ---> Returns thes current position within the file
with open('textfile.txt','r') as f:
    data=f.read(10)              # Reads the 1st 10 byte in the file
    current_position=f.tell()          # saves the current position which can be used if necessary later
    f.seek(current_position)

###     truncate()      ---> you can truncate the size of the file to a specific size
with open('textfile.txt','w')as f:
    f.write("Hi!, Nice to meet you...")
    f.truncate(4)

with open('textFile.txt','r') as f:
    print(f.read())
