def get_row(matrix, row):
        return matrix.matrix[row]

def get_column(matrix, column):
        column_array = [0] * matrix.rows
        for i in range(matrix.rows):
            column_array[i] = matrix.matrix[i][column]
        return column_array
    
def place_elements(matrix, item, row, column):
        previous = matrix.matrix[row][column]
        if(row < matrix.rows and column < matrix.columns):
            matrix.matrix[row][column] = item
            return previous
        return -1
    
def place_row(matrix, new_row, row):
        previous = matrix.matrix[row]
        if(row < matrix.rows and len(new_row) == matrix.columns):
            matrix.matrix[row] = new_row
            return previous
        return -1