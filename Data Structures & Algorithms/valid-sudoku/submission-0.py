from collections import defaultdict as dd
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = dd(set)
        cols = dd(set)
        grid = dd(set)

        for i, _ in enumerate(board):
            for j, digit in enumerate(board[i]):
                if digit == '.':
                    continue

                if digit in rows[i]:
                    return False
                if digit in cols[j]:
                    return False
                if digit in grid[tuple([i//3,j//3])]:
                    print(i, j)
                    print(tuple([i//3,j//3]), digit)
                    return False

                rows[i].add(digit)
                cols[j].add(digit)
                grid[tuple([(i//3),(j//3)])].add(digit)
        return True