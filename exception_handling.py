# _____syntax error______
# amount=1000
# if amount>2999
# print("eligible")


# ____try and except statement____
# a=[1,2,3]
# try:
#     print("Second element=",a[1])
#     print("Fourth element is",a[3])
# except:
#     print("An error occured")

#______Catching Specific Exception_____
# a=[1,2,3]
# try:
#      print("Second element=",a[1])
#      print("Fourth element is",a[3])    
# except IndexError:
#      print("Index")
# except ValueError:
#      print("value")

# def fun(a):
#     if a<4:
#         b=a/(a-3)
#     print ("value of b=",b)
# try:
#     fun(3)
# except ZeroDivisionError:
#     print("zero division error")
# except NameError:
#     print("NameError")

#____try with else clause___
# def AbyB(a,b):
#     try:
#         c=((a+b))/(a-b)
#     except ZeroDivisionError:
#         print("a/b result is 0")
#     else:
#         print(c)
# AbyB(2.0,3.0)
# AbyB(3.0,3.0)

#___finally Keyword_____
# try:
#     k=5//0
#     print(k)
# except ZeroDivisionError:
#     print("can't divide by zero")
# finally:
#     print("This always executes")

#____raising exception________
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
    raise

