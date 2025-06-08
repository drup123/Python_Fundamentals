word = "donkey"

with open("don.txt","r") as f:
    content = f.read()
    
newcon = content.replace(word,"#####")

with open("don.txt","w") as f:
    f.write(newcon)