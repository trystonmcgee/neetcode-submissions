class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        for k in range(len(nums)):
            increasing = 1
            i = k
            j = k + 1
            while j < len(nums) and nums[i] < nums[j]:
                increasing += 1
                i += 1
                j += 1
            
            decreasing = 1
            i = k
            j = k + 1
            while j < len(nums) and nums[i] > nums[j]:
                decreasing += 1
                i += 1
                j += 1
                
            ans = max(ans, increasing, decreasing)

        return ans