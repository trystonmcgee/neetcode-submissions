class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(arr, left, right):
            if left <= right:
                mid = (left + right) // 2
                
                if arr[mid] == target:
                    return mid
                
                elif arr[mid] > target:
                    return binary_search(arr, left, mid - 1)
                
                else:
                    return binary_search(arr, mid + 1, right)
            
            else:
                return left
            
        return binary_search(nums, 0, len(nums) - 1)
                