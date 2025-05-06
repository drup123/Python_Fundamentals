# lists are mutable

list = ["drup",35,94.8,"mango",90]
list.append(88)
print(list)
list.insert(4,"dadu")
print(list)
list.remove('drup')
print(list)
list.pop(2)
print(list)
list[0] = 41
print(list)