class Matrix:
    def __init__(self, size): ## creates empty matrix of given size
        self.size = size
        self.matrix = [[0 for i in range(size)] for i in range(size)] # creates empty 2d array of appropriate size

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

    def copy_matrix(self):
        size = self.size

        newmatrix = Matrix(size)

        for i in range(size):
            for j in range(size):
                newmatrix.matrix[i][j] = self.matrix[i][j]

        return newmatrix

    def det(self, total=0):
        indices = list(range(len(self.matrix)))

        # base case with 2x2
        if self.size == 2:
            val = self.matrix[0][0] * self.matrix[1][1] - self.matrix[1][0] * self.matrix[0][1]
            return val

        # get rid of minors for each item in first row, get matrix and add to total
        for focus in indices:  # for each focus column, find the submatrix ...
            As = self.copy_matrix()  # make a copy, and ...
            As.matrix = As.matrix[1:]  # ... remove the first row
            As.size -= 1
            height = len(As.matrix)

            for i in range(height):  
                As.matrix[i] = As.matrix[i][0:focus] + As.matrix[i][focus+1:]  

            sign = (-1) ** (focus % 2)  
            sub_det = As.det()  # recursively call det
            total += sign * self.matrix[0][focus] * sub_det  
        return total
    def add(self, other, other1):

      for i in range(len(self.matrix)):  
        for j in range(len(self.matrix[0])):

          self.matrix[i][j] = other1.matrix[i][j] + other.matrix[i][j]

      return self

                
m1 = [[0,0,0],[0,0,0],[0,0,0]]
m2 = [[1,1,4],[3,1,4],[6,2,2]]
m3 = [[2,2,5],[4,2,5],[7,3,3]]
m = Matrix.new(m2)
n = Matrix.new(m3)
o = Matrix.new(m1)
m.print()
print(m.det())

o = o.add(m,n)
o.print()




