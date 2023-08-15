print("Hello World!!")      #Basic print with string output
print(5)                    #Basic print with int output
print("bye",7)              #print can print multiple datatypes
print(5*5)                  #print can handle basic math operations

''' Multiple
Line
Comment'''                                  # This works with single or double Quotes
## Escape Sequence Characters ##            --> To insert characters that cannot be used directely in a string
print("Hi \nGood Morning!!")                #\n--> New Line
print('Hi guys..."Greetings!!"')            #\" OR \'--->Inserts quote in the output text  
print("Hi guys...\"Greetings!!\"")
print('''Hello                              
      how are you?''')                      # triple quotes help in printing multiple lines

print("Hey", 6, 7, sep="|", end="last\n")     # SEP-->Seperates the print elements; END--> prints the given string at the end of output string

a=4
b=10
print(f"{a} is smaller then {b}")          # You can directly make use of variables in print statement using %s (or) format (or) f-string
print("{0} is smaller than {1}".format(a,b))
print('%s is smaller than %s' % (a,b))

print("THE_END")