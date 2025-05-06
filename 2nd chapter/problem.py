letter = ''' Dear name \nYou are selected\njoining Date is date'''

naav = input("Enter your name : ")
final = letter.replace('name',naav)
finall = final.replace('date','27-2025')

print(finall)