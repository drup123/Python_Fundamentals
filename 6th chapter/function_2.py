n1 = int(input("Enter 1st number : "))
n2 = int(input("Enter 2nd number : "))
n3 = int(input("Enter 3rd number : "))


def avg(num1,num2,num3,last="finish"):
    a = (num1+num2+num3)/2
    print(last)
    return a


d = avg(n1,n2,n3,"done")
print(d)