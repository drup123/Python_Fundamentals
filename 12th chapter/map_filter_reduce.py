from functools import reduce

#map Example
l = [1,2,5,6,8,7]
m = [4,5,6,8,2,7]
print("for map")

def sum(n,p):
    return n+p
sumList = map(sum,l,m)
print(f"this is map for sum (we need to consider 2 list) : {list(sumList)}")

sqr = lambda x:x*x
sqrList = map(sqr,l)
print(list(sqrList))


#Filter example
print("\nfor Filter")

def even(k):
    if k%2 == 0:
        return True
    return False
onlyEven = filter(even,l)
print(list(onlyEven))

#Reduce Example
print("\nfor reduce")

def sum2(a,b):
    return a+b
print(f"Reduce do operation on list element one by one {reduce(sum2,l)}")
