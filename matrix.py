class Matrix:
    def __init__(self, size): ## creates empty matrix of given size
        self.size = size
        self.matrix = [[0]*size]*size # creates empty 2d array of appropriate size

    def new(matrix): # expects a 2d array as input, creates a matrix object
        size = len(matrix)
        m = Matrix(size)
        m.matrix = matrix
        return m

    def print(self):
        for row in self.matrix:
            print(row)


    # returns the matrix when the minors at x, y are removed
    def minors(self, x, y):
      
      
    def det(self):
      

m1 = Matrix(2,3)

m1.print()

m2 = Matrix.new([[0,1,2],[3,4,5]])

m2.print()
