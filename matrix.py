class Matrix:
    def __init__(self, rows, cols): ## creates empty matrix of given size
        self.rows = rows
        self.cols = cols
        self.matrix = [[0]*cols]*rows # creates empty 2d array of appropriate size

    def new(matrix): # expects a 2d array as input, creates a matrix object
        rows = len(matrix)
        cols = len(matrix[0])
        m = Matrix(rows, cols)
        m.matrix = matrix
        return m

    def print(self):
        for i in self.matrix:
            print(i)


m1 = Matrix(2,3)

m1.print()

m2 = Matrix.new([[0,1,2],[3,4,5]])

m2.print()
