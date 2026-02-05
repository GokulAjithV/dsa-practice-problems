# 1. Star Pattern
# Number of rows and columns should be given in the input

def matrix_pattern(row_count, column_count):
    for i in range(row_count):
        for j in range(column_count):
            print("*", end="")
        print()

# 2. Right angle pattern        

def right_angle_pattern(row_count):
    for i in range(row_count):
        for j in range(i + 1):
            print("*", end="")
        print()
