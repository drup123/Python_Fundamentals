def acting(status):
    match status:
        case 500:
            return "earn more"
        case 2000:
            return "its ok"
        case 10000:
            return "excellent"
        case _:
            return "something is wrong"
        
a = int(input(" entr salary : "))
print(acting(a))
