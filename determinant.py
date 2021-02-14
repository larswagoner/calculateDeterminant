#the input must be structured in the following way
#Each column separated by a space, each row by a new line, 
#and each matrix by an equals sign.


def minor_matrix(m, i, j):
    return [row[:j] + row[j + 1:] for row in m[:i] + m[i + 1:]]


#converts matrix into readable string
def convert_matrix(m):
    matrix = ''

    for row in m:
        matrix += '\n'
        for value in row:
            matrix += str(value) + ' '

    return matrix


def read_matrix(s):
    result = []
    lines = s.splitlines()

    for line in lines:
        result += [[int(number) for number in line.split()]]

    return result


def calculate_determinant(matrix):
    if len(matrix[0]) == 1:
        return matrix[0][0]

    if len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    terms = [((-1) ** j) * matrix[0][j] * calculate_determinant(minor_matrix(matrix, 0, j)) for j in range(0, len(matrix[0]))]
    determinant = sum(terms)

    return determinant


def start_determinant(file_name):
    matrices = open(file_name).read().split('=\n')

    for matrix in matrices:
        matrix = read_matrix(matrix)
        determinant = calculate_determinant(matrix)

        print('The determinant of the matrix' + convert_matrix(matrix) + '\nis %d.\n' % determinant)


#start
file_name = input('Enter the input file name: ')
start_determinant(file_name)