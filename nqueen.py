# n: int for chessboard size
def n_queens(n):
    # This function uses depth-first search to find all possible solutions to the n-queens problem.
    def DFS(queens, xy_dif, xy_sum):
        # queens is a list of column positions for each queen on the board.
        # xy_dif and xy_sum are lists used to check if a queen can be placed in a given position.
        # p is int representing the current row being considered on the board.
        p = len(queens)
        if p == n:
            # If all queens have been placed on the board, add the solution to the result list.
            result.append(queens)
            return None
        # q is int representing the current column being considered on the board.
        for q in range(n):
            # For each column on the board, check if a queen can be placed in that position.
            #  q not in queens : if the column (q) is already occupied by another queen
            # p - q not in xy_dif and p + q not in xy_sum : to check for diagonals are occupied.
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                # If the position is valid, place a queen there and continue the search.
                # conditions to check if queen can't be placed -
                # If a queen is placed in position (p, q), then p - q is added to xy_dif
                # f a queen is placed in position (p, q), then p + q is added to xy_sum
                DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])
    # list of lists with all possible solutions
    result = [] # empty list to store all solutions
    DFS([], [], []) # 3 empty lists- initial state of: board, xy_dif, xy_sum
    return result

def solve_n_queens(n):
    # This function takes the solutions returned by n_queens and formats them into a more readable output.
    # list of lists with all possible solutions
    solutions = n_queens(n)
    output = []
    # sol is a list of integers representing a single solution to the n-queens problem.
    for sol in solutions:
        board = [] # list of strings representing a single solution in a more readable format.
        # i is an int representing the current row being considered on the board when formatting a solution.
        for i in range(n):
            # row is a list of characters representing a single row on the chessboard when formatting a solution.
            row = ['.'] * n
            row[sol[i]] = 'Q'
            board.append(''.join(row))
        output.append(board)
    print(f'{len(solutions)} solutions')
    return output

print(n_queens(8))
print(solve_n_queens(8))
# time complexity O(N!) space O(N)