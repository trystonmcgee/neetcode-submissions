class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(lst):
            if len(lst) > 1:
                left_arr = lst[:len(lst)//2]
                right_arr = lst[len(lst)//2:]

                merge_sort(left_arr)
                merge_sort(right_arr)
    
                i = 0
                j = 0
                original_idx = 0
                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] < right_arr[j]:
                        lst[original_idx] = left_arr[i]
                        i += 1
                    else: 
                        lst[original_idx] = right_arr[j]
                        j += 1

                    original_idx += 1

                while i < len(left_arr):
                    lst[original_idx] = left_arr[i]
                    i += 1
                    original_idx += 1
    
                while j < len(right_arr):
                    lst[original_idx] = right_arr[j]
                    j += 1
                    original_idx += 1

        merge_sort(nums)
        return nums


    
