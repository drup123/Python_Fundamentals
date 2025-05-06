# string is a unmutable

name = "Drup Patil"
name2 = name[:4]
name3 = name[:]
print(name2)
print(name3)
print(name[-1:])
print(name[-5:-1])
print(name[:-5])

# Skipping value
print(name[1:5:2]) 

# Functions
print(name.endswith('il'))
print(name.startswith('il'))

# replace , find

#f STRING

naav = input("enter your name")
print(f"good afternoon {naav}")