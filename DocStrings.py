### Python Docstrings are the string literals that apper right after the definition of a function,method,class or module.
##  --> It is the documentation which explains the particular block
##  --> A Valid doc string should always be given right below the function definition & above the func code.

def square(n):
    '''Takes in anumber and returns its square'''           # DocString is NOT a comment!!
    print(n**2)

square(5)
print(square.__doc__)

###     PEP8        ###
##  ---> It is a documentation which provides guidlines andbest practices on how to write python code.
##  ---> Its focus is to increase readablility & consistency of python code.
##  ---> PEP-- Python Enhancement Proposal

# The Zen of Python, by Tim Peters---->import this

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!