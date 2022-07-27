def generateTensorProduct(matrix_a, matrix_b):
    tensor_matrix = []
    temp_matrix = []
    count = len(matrix_b)
    for element_a in matrix_a:
        counter = 0
        check = 0
        while check < count:
            for num_a in element_a:
                for num_b in matrix_b[counter]:
                    temp_matrix.append(num_a * num_b)
            counter += 1
            tensor_matrix.append(temp_matrix)
            temp_matrix = []
            check +=1

    print('\nTensor Product Matrix is: \n')
    for item in tensor_matrix:
        print(item)
    print()

    return tensor_matrix

def generateMatrix(matrix_rows, matrix_columns):
    matrix = [ [ 0 for j in range(matrix_columns) ] for i in range(matrix_rows) ]

    for i in range(matrix_rows):
        for j in range(matrix_columns):
            matrix[i][j] = float(input(f'Enter the value of the element ({i},{j}): '))

    print('MATRIX: ')
    for line in matrix:
        print(line)

    return matrix


def main():
    print('Generating Tensor Product Matrix....')
    matrix_a_rows = int(input('Enter the number of rows of the First matrix: '))
    matrix_a_columns = int(input('Enter the number of columns of the First matrix: '))
    print('Fist Matrix is...')
    matrix_a = generateMatrix(matrix_a_rows, matrix_a_columns)
    matrix_b_rows = int(input('Enter the number of rows of the Second matrix: '))
    matrix_b_columns = int(input('Enter the number of columns of the second matrix: '))
    print()
    print('Second Matrix is')
    matrix_b = generateMatrix(matrix_b_rows, matrix_b_columns)
    print()
    generateTensorProduct(matrix_a, matrix_b)


if __name__ == '__main__':
    main()