class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0]*cols]*rows # creates empty 2d array of appropriate size


    def print(self):
        for i in self.matrix:
            print(i)


m1 = Matrix(2,3)

m1.print()
