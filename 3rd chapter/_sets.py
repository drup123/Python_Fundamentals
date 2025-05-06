# # EMPTY SET
r = set()

i = input("enter an element :")
j = int(input("enter an element :"))
r.add(i)
r.add(j)
print(r)

s  = {1,4,45,}
s.add("dadu")
print(s,type(s))
print(s.union(r))
print(s.intersection(r))


#PROBLEM
set = {20,20.0,"20"}
print(len(set))