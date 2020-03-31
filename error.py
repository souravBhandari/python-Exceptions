'''c=a+b,syntax errors if b is not defined , they are traced in developement phase

1 syntax errors
2 logical errors,finded in test cases,extensive debugging
3 run time errors(exception) ,occurs in execution time,exception is thrown and program is terminated
     syntax:
try:
    statement(s)
except:
    statement(s)
finally:
    statement(s)

'''
try:    
    a=int(input("enter a no"))
except:
   a=int(input("try again"))
try:
    b=int(input("enter second no"))
except:
    b=int(input("try again"))

c=a+b
print(c)