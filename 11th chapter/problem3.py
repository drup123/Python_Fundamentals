o = int(input("Enter any number : "))
# l = [1,2,3,4,5,6,7,8,9,10]
# list = [o*i for i in l]
# print(list)

table = [o*i for i in range(1,11)]
print(table)

with open("tab.txt","w") as f:
    f.write(str(table))