class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)*len(matrix[0])-1
        while left <= right:
            mid = left + (right - left) // 2
            c = mid % len(matrix[0])
            r = mid // len(matrix[0])
            val = matrix[r][c]
            if val == target:
                return True
            elif val > target:
                right = mid-1
            else:
                left = mid+1
        return False