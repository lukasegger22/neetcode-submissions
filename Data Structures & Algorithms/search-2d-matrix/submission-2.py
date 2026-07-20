class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix)*len(matrix[0]))-1
        COLS = len(matrix[0])
        while left <= right:
            mid = (left+right)//2
            r = mid // COLS
            c = mid % COLS
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid+1
            else:
                right=mid-1
        return False