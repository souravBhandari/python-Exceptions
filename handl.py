try:
    a=int(input("enter a"))
    print("A=:",a)
except:
    a=int(input("try again"))
    print("A=:",a)
finally:
    print("thank you") # if error occurs in except block themn also finally will be executed.
    
