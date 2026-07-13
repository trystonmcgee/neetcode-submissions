class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        og = nums

        sorted = nums[:]
        sorted.sort()

        reversed = nums[:]
        reversed.sort(reverse=True)

        if og == sorted or og == reversed:
            return True
        return False
        
