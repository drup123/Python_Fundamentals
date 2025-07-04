# a = int(input("enter the 1st no : "))
# b = int(input("enter the 2nd no : "))

# if(b == 0):
#     raise ZeroDivisionError("This is invalid")
# else:
#     print(a/b)


try:
    a = int(input("enter the 1st no : "))
    b = int(input("enter the 2nd no : "))
    print(a/b)

except ZeroDivisionError as z:
    print(z)
    print("you cant divide by zero")


   


