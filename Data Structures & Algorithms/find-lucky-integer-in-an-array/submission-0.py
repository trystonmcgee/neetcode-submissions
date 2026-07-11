from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        nums = set(arr)
        cnts = Counter(arr)
        res = -1

        for num in nums:
            if cnts[num] == num and num > res:
                res = num
        
        return res