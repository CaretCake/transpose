def transpose_matrix(matrix):

    row_count = len(matrix)
    col_count = len(matrix[0])
    transposed_matrix = [[] for i in range(col_count)]

    for current_column in range(col_count):
        for current_row in range(row_count):
            transposed_matrix[current_column].append(matrix[current_row][current_column])

    return transposed_matrix
