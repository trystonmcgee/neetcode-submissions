class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        new = [str(num) for num in nums]
        string = "".join(new)
        cons = string.split("0")

        max = 0
        for string in cons:
            if len(string) > max:
                max = len(string)
        
        return max 


