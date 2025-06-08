class table:
    n = 5
    for i in range(1,11):
        print(f"{i*n}")
    name = "Drup"          #class attributes
    surname = "Patil"
    birth = 28
padha = table()
padha.father = "shivaji"   #instance attribute
padha.birth = 27           #first priority to instance attribute
print(padha.name)
print(padha.father)
print(padha.surname)
print(padha.birth)