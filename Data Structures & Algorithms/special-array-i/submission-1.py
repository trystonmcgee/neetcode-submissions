class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        
        res = True
        for i in range(1, len(nums)):
            if nums[i] % 2 != nums[i - 1] % 2:
                continue
            else:
                res = False
                break
            
        return res
            
