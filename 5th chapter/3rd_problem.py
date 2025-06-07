u = int(input("Enter the number : "))

for i in range(2,u):
    if(u%i) == 0:
        print(u," this number is not prime")
        break
    else:
        print(u," this number is prime")
        break