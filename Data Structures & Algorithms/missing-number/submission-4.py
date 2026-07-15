class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ran = [num for num in range(0, len(nums) + 1)]
        cnts = {}

        for num in nums:
            if num not in cnts:
                cnts[num] = 1
            else:
                cnts[num] += 1
        
        for num in ran:
            if num not in cnts:
                cnts[num] = 1
            else:
                cnts[num] += 1
        
        print(cnts)
        
        for num, cnt in cnts.items():
            if cnt == 1:
                return num