def readint():
    while(True):
        try:
            a=int(input("enter a no"))
            return a
        except:
            print("pls try again")
a=readint()
b=readint()
c=a+b
print(c)