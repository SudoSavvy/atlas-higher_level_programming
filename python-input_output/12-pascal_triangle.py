#!/usr/bin/python3
"""
This module defines the function `pascal_triangle` that returns
a list of lists representing Pascal's triangle up to n rows.

Pascal's Triangle:
- The triangle starts with a single 1 at the top.
- Each subsequent row starts and ends with 1.
- Each number inside the row is the sum of the two numbers directly above it.
- For example, Pascal's triangle of 5 rows is:
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    [1, 4, 6, 4, 1]

Functions:
- pascal_triangle(n): returns a list of lists representing Pascal's triangle of size n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of size n.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        List of lists, where each inner list represents a row in Pascal's triangle.
    """
    # If n is less than or equal to 0, return an empty list as Pascal's triangle doesn't exist for such cases.
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row being [1].
    triangle = [[1]]

    # Build each row of the triangle, starting from the second row up to the nth row.
    for i in range(1, n):
        # Start each row with a '1' (since Pascal's triangle rows always begin with 1).
        row = [1]
        
        # Previous row is the last row in the triangle at this point.
        prev_row = triangle[i - 1]

        # Fill in the middle elements of the row.
        # Each element is the sum of the two numbers directly above it from the previous row.
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        # End each row with a '1' (since Pascal's triangle rows always end with 1).
        row.append(1)
        
        # Add the completed row to the triangle.
        triangle.append(row)
    
    # Return the complete Pascal's triangle.
    return triangle
