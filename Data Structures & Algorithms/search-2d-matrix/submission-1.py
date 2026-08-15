class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def ind_to_pos(ind: int) -> tuple:
            num_cols = len(matrix[0])
            return (ind // num_cols, ind % num_cols)

        l = 0
        r = len(matrix)*len(matrix[0])-1
        while l<=r:
            mid = (l+r)//2
            row, col = ind_to_pos(mid)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l=mid+1
            else:
                r=mid-1
        return False