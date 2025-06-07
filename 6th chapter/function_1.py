naav = input("Enter your name please : ")
vay = int(input("Enter your age : "))


def check(name,age):
    if(age>18):
        print(f"{name} You can visit this site , Thank you")
    else:
        print(f"{name} You can't visit , sorry")


check(naav,vay)
