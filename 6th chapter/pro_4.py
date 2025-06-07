l = int(input("Enter any number : "))

def pattern(l):
    if(l == 0):
        return
    print("*"*l,end="")
    print("\n")
    pattern(l-1)

pattern(l)