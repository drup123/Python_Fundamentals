n1 = int(input("enter the 1st number : "))
n2 = int(input("enter the 2nd number : "))
n3 = int(input("enter the 3rd number : "))

def maxmin(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print(f"{n1} is greatest")
    elif(n2>n1 and n2>n3):
        print(f"{n2} is greatest")
    else:
        print(f"{n3} is greatest")

maxmin(n1,n2,n3)