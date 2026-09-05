class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                leftPrefix = matrix[r][c-1] if c>0 else 0
                topPrefix = matrix[r-1][c] if r>0 else 0
                topLeftPrefix = matrix[r-1][c-1] if (r> 0 and c>0) else 0
                self.matrix[r][c] = (leftPrefix + topPrefix) - topLeftPrefix + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        leftPrefix = matrix[row2][col1-1] if col1>0 else 0
        topPrefix = matrix[row1-1][col2] if row1>0 else 0
        topLeftPrefix = matrix[row1-1][col1-1] if (row1>0 and col1>0) else 0

        #print(leftPrefix)
        #print(topPrefix)
        #print(topLeftPrefix)
        #print()
        return matrix[row2][col2] - (leftPrefix + topPrefix) + topLeftPrefix


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)