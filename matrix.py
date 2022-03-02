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
        print("[")
        for row in self.matrix:
            print("  ", row)
        print("]")


    # returns the matrix when the minors at x, y are removed
    def minors(self, row, col):
        minors = Matrix(self.size - 1)

        for (i,v) in enumerate(self.matrix):
            for (j, value) in enumerate(v):
                if i != row and j != col:
                    print(i - (i > row),j - (j > col), ": ", value)
                    minors.matrix[i - (i > row)][j - (j > col)] = value
                    # TODO: modifies more than one row at a time
                    minors.print()
        minors.print()
        return minors

        
    def det(self):
        print(self.size, len(self.matrix), len(self.matrix[0]))
        if self.size < 2:
            return self.matrix[0][0]
        elif self.size == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            sum = 0
            for (i,v) in enumerate(self.matrix[0]): # loop through first row
                sum += ((-1) ** i) * self.minors(0,i).det()
            return sum
                
m2 = Matrix.new([[0,1,4,32],[3,1,4,40],[6,0,2,32],[3,1,6,60]])

m2.print()

m2.minors(1,1).print()

# print(m2.det())

# twoxtwo = Matrix.new([[1,2],[3,4]])
# twoxtwo.print()
# print(twoxtwo.minors(0,0).det())



