'''
stone = 1
paper = -1
sesior = 0
'''

import random
com = random.choice([1,-1,0])
my = input("enter your choice : ")
my_dict = {'s' : 1,'p' : -1,'se' : 0}
com_dict = {1 : 'stone' , -1 : 'paper' , 0 : 'sesior'}
my_choice = my_dict[my]

print(f"your choice is {com_dict[my_choice]}\nComputer choose {com_dict[com]}")

if(com == my_choice):
    print("Draw")
elif(com == -1 and my_choice == 1):
    print("You loose")
elif(com == -1 and my_choice == 0):
    print("You Win")
elif(com == 1 and my_choice == -1):
    print("You Win")
elif(com == 1 and my_choice == 0):
    print("You loose")
elif(com == 0 and my_choice == 1):
    print("You Win")
elif(com == 0 and my_choice == -1):
    print("You loose")
else:
    print("something is wrong")
