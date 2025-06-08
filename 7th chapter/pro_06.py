with open("log.txt","r+") as f:
    c = f.read()
    print(c)
if("python" in c):
    print("yes")
else:
    print("no")