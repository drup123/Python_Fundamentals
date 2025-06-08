class checking:
    name = "tony"
    age = 40
    income = "Billions"
    @staticmethod
    def __init__(name,age,income):    #This is dunder method called automatically when we create obj
        name = name
        age = age
        income = income
        print(name)
        print(age)
        print(income)
        print("this is my world")


h = checking("thor",1500,"infinity")
print(h.name)
print(h.age)
print(h.income)    
        