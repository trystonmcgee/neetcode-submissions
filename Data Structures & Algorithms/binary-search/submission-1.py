class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right, lst):
            mid = (left + right) // 2

            if target not in nums:
                return -1

            elif nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                return binary_search(0, mid, nums)
            
            elif nums[mid] < target:
                return binary_search(mid + 1, right, nums)
        
        return binary_search(0, len(nums), nums)