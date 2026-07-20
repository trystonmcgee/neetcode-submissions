class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for lst in matrix:
            for num in lst:
                if num == target:
                    return True
        
        return False
                