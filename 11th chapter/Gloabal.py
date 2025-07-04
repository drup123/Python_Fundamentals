i = 78    #This is global variable

def demo():
     global i    #it convert global to local
     i = 7       #this is local variable
     print(i)

demo()
print(i)