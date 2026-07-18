class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        i = 0
        j = i + 1
        while i < len(numbers) or j < len(numbers):
            if j < len(numbers):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                else:
                    j += 1
            
            else:
                i += 1
                j = i + 1
        



