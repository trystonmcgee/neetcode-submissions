class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        copy = [num for num in nums]
        
        for num in copy:
            nums.append(num)

        return nums