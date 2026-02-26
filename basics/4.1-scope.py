# 4.1-scope.py
# Built in: print(), len(), and range()
# Local (L): Variables defined inside the current function or lambda. These are created when the function is called and destroyed when it finishes.
# Enclosing (E): Found in nested functions; these are variables in the outer (enclosing) function's scope.
# Global (G): Variables defined at the top level of a script or module. They are accessible throughout the entire file.
# Built-in (B): Pre-defined names in Python, such as print(), len(), and range(), which are always available.

def f1():
    print("-----------------inside f1")
    name="Ninad"
    def f2():
        print(name)
        print("-------------inside f2")
        city="mumbai"
        def f3():
            global name 
            name="Rahul"
            print("-----------------inside f3")
            print(name)
            nonlocal city
            city="pune"
            print(city)
        f3()
    f2()
    
f1()

print()