class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        print(f"2D vectors are {i}i {j}j")


class ThreeDvector:
    def __init__(self,i,j,k):
        super().__init__()
        self.k = k

        print(f"3D vectors are {i}i {j}j {k}k")

h = TwoDvector(5,6)
u = ThreeDvector(5,6,8)

