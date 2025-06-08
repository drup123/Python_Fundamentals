import math

class Calculator:
    def main(self,n):
        print(f"squre of {n} is = {n**2}")
        print(f"cube of {n} is = {n**3}")
        print(f"squre root of {n} is = {n**1/2}")


i = int(input("enter the number : "))

g = Calculator()
g.main(i)
