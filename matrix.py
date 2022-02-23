from turtle import left
from vector import Vector

class Matrix():
    # Empty initialization
    '''
    def __init__(self):
        self.matrix = []
        '''
    
    '''
    def __init__(self, matrix, rows, columns):
        self.matrix = matrix
        self.rows = rows
        self.columns = columns
    '''
    
    
    # Initialize with rows and columns
    def __init__(self, rows, columns, matrix = None):
        if not matrix == None:
            self.matrix = matrix
        
        else:
            self.rows = rows
            self.columns = columns
            matrix = [0] * rows
            #i=0
            for i in range(rows):
                matrix[i] = [0] * columns
                i += 1
            self.matrix = matrix
        
    # If there is already a multi-dimensional array    
    def fill_matrix(self, matrix):
        self.matrix = matrix
    
    #def __init__(self, matrix):
    #    self.matrix = matrix

    def get_row(self, row):
        return self.matrix[row]
    
    def get_column(self, column):
        column_array = [0] * self.rows
        for i in range(self.rows):
            column_array[i] = self.matrix[i][column]
        return column_array
    
    def place_element(self, item, row, column):
        previous = self.matrix[row][column]
        if(row < self.rows and column < self.columns):
            self.matrix[row][column] = item
            return previous
        return -1
    
    def place_row(self, new_row, row):
        previous = self.matrix[row]
        if(row < self.rows and len(new_row) == self.columns):
            self.matrix[row] = new_row
            return previous
        return -1
    
    def place_column(self, new_column, column):
        previous = [0] * self.rows
        for i in range(self.rows):
            previous[i] = self.matrix[i][column]
            self.matrix[i][column] = new_column[i]
        return previous
    
    def place_vector_column(self, vector, column):
        previous = [0] * self.rows
        for i in range(self.rows):
            previous[i] = self.matrix[i][column]
            self.matrix[i][column] = vector.get(i)
        return previous
    
    def scale(self, k):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = self.matrix[i][j] * k
        return
    
    # Elementary Methods for REF
    def scale_row(self, row, k):
        if(row > self.rows):
            return -1
        for i in range(self.columns):
            self.matrix[row][i] = k * self.matrix[row][i]
        return
    
    # row1 is incrimented by row2
    def add_row(self, row1_pos, row2_pos):
        row1 = self.get_row(row1_pos)
        row2 = self.get_row(row2_pos)

    
    # Helper method for REF
    def left_zeros(row, pos):
        i = pos -1
        while i >= 0:
            if row[i] != 0:
                return False
            i = i-1
        return True


    # TO DO
    def ref(self):
        for i in range(self.rows):
            row = self.get_row(i)
            while not Matrix.left_zeros(row, i):
                return

    
    

    
    def __str__(self):
        string = ""
        for i in range(self.rows):
            string = string + ' '.join(str(num) for num in self.matrix[i]) + "\n"
        return string
    
    # Static Methods
    def multiply_vector(matrix, vector):
        if not matrix.columns == vector.length:
            return
    
        print(result)
        for i in range(vector.length):
            temp = Vector(matrix.get_column(i))
            temp.scale(vector.get(i))
            result = Vector.add(result, temp)
        
        return result

    def multiply_matrix_test(matrix1, matrix2):
        if not(matrix1.columns == matrix2.rows):
            return -1
        
        result_matrix = Matrix(matrix1.rows, matrix2.columns)
        for i in range(matrix1.rows):
            results = [0] * matrix2.columns
            for j in range(matrix2.columns): 
                sum = 0
                for k in range(matrix2.rows):
                    sum = sum + (matrix1.get_row(i)[k] * matrix2.get_column(j)[k])
                results[j] = sum
            result_matrix.place_row(results, i)
        
        return result_matrix

'''test1 = Matrix(2,2)
test1.place_row([2,1], 0)
test1.place_row([3,1], 1)
'''

test2 = Matrix(3,3)
test2.place_element(12, 1, 2)
print(test2)




