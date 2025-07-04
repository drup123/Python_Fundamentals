from typing import Tuple,Union,List,Dict

a : List[int] = [1,2,3,4]

b : Tuple[int,str] = ('Drup',20)

c : Dict[str,int] = {"rohit" : 20 ,"samadhan" : 20}

d : Union[int,str] = "eytf654t"


t = {'a' : 1,'b' : 2}
y = {'c' : 3,'d' : 4}

merged = t | y
print(merged)