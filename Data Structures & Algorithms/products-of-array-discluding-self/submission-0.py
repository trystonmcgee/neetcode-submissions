import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        cycles = len(nums)
        res = []

        while cycles > 0:
            nums[0], nums[i] = nums[i], nums[0]
            others = nums[1:]
            product = math.prod(others)
            res.append(product)
            i += 1
            cycles -= 1
        
        return res