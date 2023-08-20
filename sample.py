def greet(fx):
    def mfx():
        print("Good Morning !!")
        fx()
        print("Thanks for you visit !!")
    # return mfx

@greet
def hello():
    print("Hello World")


# greet(hello())
hello()