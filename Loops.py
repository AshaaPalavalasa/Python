###     Loops are used to execute a group of statements a certain number of times.      ###
###      FOR LOOP & WHILE LOOP      ###
###         FOR LOOP --->    can iterate over a sequence of iterable objects 

name="Swaroopa"
for i in name:
    if(i=='r'):
        print("We came HalfWay!!")

colors=["Black","Blue","Brown"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(10):                 #Starts from 0 to 9
    print(k)

for k in range(1,15):               #Starts from 1 to 14
    if k%2==0:
        print(k,"is EVEN!!!")

for k in range(1,20,5):             #Starts from 1 to 20 and steps the k value by 5
    print(k)

for i in range(7):
    print(i*2)
else:
    print("You have reached the end of the loop")       # The statements in the else block will be executed after all iterations are completed.

# If break is used in if or while loop, else doesnot execute, ELSE is ONLY EXECUTED IF THE LOOP IS COMPLETED NOT BREAKED




###         WHILE LOOP  ---> Performs a set of code until the condition is True.        ###

i=0
while(i<=8):
    print(i)
    i=i+1

count=5
while(count>-2):
    print(count)
    count-=1
else:
    print("You are done with the loop")

####        Break & Continue         ####
##  BREAK   ---> Terminates the loop at a particular iteration  --->Exits the loop
##  CONTINUE    ---> Skips the particular iteration in a loop   --->Exits the iteration

for i in range(12):
    if(i==10):
        print("Breaking out of the loop")
        break
    elif(i>=5 and i<=7):
        print("Iteration is skipped")
        continue
    else:
        print(i)


i=0
while True:
    print(i)
    i=i+1
    if(i%8==0):
        break