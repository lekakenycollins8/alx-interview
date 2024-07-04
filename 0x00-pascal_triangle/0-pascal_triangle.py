#!/usr/bin/python3
"""function that generates the Pascal's triangle"""


def pascal_triangle(n):
    """takes in an integer and returns a list of lists"""
    triangle = []

    if n <= 0:
        return []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle
