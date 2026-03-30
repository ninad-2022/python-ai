# Error handling:
#   - managing the expection (runtime error) to prevent unexpected
#     termination or crash of the application

# Error vs Expection
#   -   Exception is an error that occurs during execuation 

# name="mahesh"
# try:
#     name=="mahesh"
#     print("hii")
# except: #it works like a catch. we can write multiple except

# else: 
#     print("erro")

# finally:
#     print("i am always")

try:
    print("Begning")
    city="Pune"
    print(city) #NameError
    # print(10/0) #ZeroDivisionError
    
    a=[]
    # a[3]=40 #InedxError 

    b={"aa":"AA"}
    # print(b["cc"]) #keyError

    #city() #TypeError
    print("ending")
except NameError as err:
    print("Declare and initialize: ", err)

except ZeroDivisionError as err:
    print("Do not divide key by Zero: ", err)

except (KeyError, TypeError, IndexError) as err:
    print("Error: ", err)

except (Exception) as err:
    print("Something went wrong:", err)

else:
    print("Success Message")
finally:
    print("Finally, always executes...")