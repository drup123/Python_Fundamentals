degree = int(input("Enter Degree in Celsius : "))

def convert(degree):
    return degree*(9/5)+32

a = convert(degree)
print(f"{degree} : Degree Celsius")
print(f"{a} : Dgree Fahrenheit")