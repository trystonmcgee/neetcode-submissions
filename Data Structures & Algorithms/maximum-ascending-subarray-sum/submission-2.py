class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                res.append(curr)
                curr = nums[i]
            
        res.append(curr)
        return max(res)