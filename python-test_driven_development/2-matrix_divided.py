#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number and returns a new matrix.

    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats, 
                   or rows are not of the same size, 
                   or div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix with each element divided by div.
    """

    # Check if matrix is a list of lists of integers/floats
    if (not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(elem, (int, float)) for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows are of the same size
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
