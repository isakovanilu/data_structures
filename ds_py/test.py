# create a 3x3 matrix
matrix3x3 = [[' ' for i in range(3)] for j in range(3)] # it will create an empty 3x3 list range(3):0,1,2

def update_matrix3x3(matrix3x3, row, column, value):
    row_len = len(matrix3x3) # row length
    col_len = len(matrix3x3[0]) # column lenght
    if (row >= row_len or column >= col_len) or matrix3x3[row][column] != ' ': # if the coordinates greater than matrix size return the function
        print('Please enter different coordinates')
        return
    else:
        for i in range(row_len): # loop throught rows
            for j in range(col_len): # loop throught columns
                if i == row and j == column: # if row and columns values match for the given coordinates
                    matrix3x3[i][j] = value # assign the new values for those coordinates

    return matrix3x3


## check the winner