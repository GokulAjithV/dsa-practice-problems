# Star Pattern
# Number of rows and columns should be given in the input

def matrix_pattern(row_count, column_count):
    for i in range(row_count):
        for j in range(column_count):
            print("*", end="")
        print()
        

matrix_pattern(3, 7)