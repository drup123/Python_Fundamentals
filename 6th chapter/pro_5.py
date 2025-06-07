k = int(input("Enter the number for its table : "))
o = 1
def Table(k,o):
    if(o == 0 or o == 11):
        return
    print(o*k)
    Table(k,o+1)

Table(k,o)