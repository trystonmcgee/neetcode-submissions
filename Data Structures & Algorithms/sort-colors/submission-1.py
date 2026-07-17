class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def merge_sort(arr):
            if len(arr) > 1:

                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]

                merge_sort(left)
                merge_sort(right)

                i = j = og = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[og] = left[i]
                        i += 1
                    else:
                        arr[og] = right[j]
                        j += 1
                    og += 1
                
                while i < len(left):
                    arr[og] = left[i]
                    i += 1
                    og += 1
                
                while j < len(right):
                    arr[og] = right[j]
                    j += 1
                    og += 1
        
        print(merge_sort(nums))
                


                
        