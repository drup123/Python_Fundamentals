l = int(input("enter the number of lines you want : "))

for i in range(1,l+1):
    print(" "*(l-i), end="")
    print("*"*(2*i-1),end="")
    print("\n")