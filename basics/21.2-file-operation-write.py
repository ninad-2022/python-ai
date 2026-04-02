# OPERATION 1: .write()
print("-"*20, "WRITE", "-"*20)

# this will change the whole content 
with open("file.txt", "w") as f:
    f.write("Hello World!")

# this will apend the content 
with open("file.txt", "w") as f:
    lines= ["first\n", "second\n", "third\n"]
    f.writelines(lines)


with open("abc.txt","r") as src, open("xyz.txt", "w") as dest:
    for line in src:
        dest.write(line)