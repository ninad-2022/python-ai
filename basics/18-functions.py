# functions: it is a reusable block of statements which performs specific operations for 
# making code modular redability 

# syntax:
def sum(a, b, *rest):
    print(rest)
    return a+b

sumOf = sum(2, 1, 23432423, 23, 34, 5, 34)
print(sumOf)

# function parameters: it is a varaible inside the function which is used to get accept
# input in the function, so in above example a and b are parameters.
# function arguments: they are the values passed to the function while callling it


# positional argumets:
def minus (a, b):
    return a - b
print(minus(2,1))

# default parameters 
def multi (a=1, b=1):
    return 1 * 1
print(multi(1, 1))

def addCity (city, cities):
    cities.append(city)
    return cities

print(addCity("Mumbai", []))

# variable length argument 

# *arguments 

# this is for tuple only 

# for positional arguments 

 

def add(a,b,*args):

    return sum((a,b,*args))

 

# print(add(10))

print(add(10,20))

print(add(10,20,30))

print(add(10,20,30,40))

 

# double star for keyword argument 

# **args gives dictionary

 

def add(a,b,**args):

    print(a,b)

    print(args)#{c:30, d:40}

    # return sum((a,b,*args))

 

add(10,20)

add(10,20,c=30,d=40)