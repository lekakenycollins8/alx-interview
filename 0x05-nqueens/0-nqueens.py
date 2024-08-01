#!/usr/bin/python3
from sys import argv, exit

def is_safe(board, row, col, N):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                    return False
    return True

def print_solution(board):
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)

def solve_queens(board, row, N):
    if row == N:
        print_solution(board)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_queens(board, row + 1, N)

def nqueens(N):
    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [-1] * N
    solve_queens(board, 0, N)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    nqueens(N)