w = ["ironman","Tony","timemachine"]


with open("tony.txt") as f:
    content = f.read()

for word in w:
    new = content.replace(word,"####")

with open("tony.txt","w") as f:
        
        f.write(new)