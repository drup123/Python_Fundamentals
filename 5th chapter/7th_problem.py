l = int(input("Enter the line you want to print : "))

for i in range(1,l+1):
    print("*"*i,end=" ")
    print(" "*(l-i),end=" ")
    print("\n")

