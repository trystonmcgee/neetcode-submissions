class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}

        for i, val in enumerate(nums):
            if val not in map:
                map[val] = i
            
            elif val in map and abs(i - map[val]) <= k:
                return True

            else:
                map[val] = i 
        
        return False
            
        

            
            
            