d = int(input("enter the number : "))

def sum(num):
    if(num == 1):
        return 1
    return num+sum(num-1)

print(f"{sum(d)} is sum up to {d}")
