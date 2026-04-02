# file operation 
# open(filepath, mode)

# OPERATION 1: .read()
file = open("log.py", "r")
print(file.read())
file.close()

# when you read the content it is in memory, so it used ram. but if we load a big file
# then it will add big content in ram, so will ram will get crash, so use this .read()
# method in small file only 
# NOTE: stop the close method else it will be memory leakage 

#OR

with open("log.py", "r") as file:
    print(file.read())

print("-"*30)

with open("log.py", "r") as file:
    print(file.readline())

print("-"*30)

with open("log.py", "r") as file:
    print(file.readline(10))

print("-"*30)

with open("log.py", "r") as file:
    for line in file.readlines():
        print(line)

print("-"*30)
