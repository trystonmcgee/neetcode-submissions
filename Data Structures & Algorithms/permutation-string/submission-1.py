class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        k = len(s1)
        s1 = sorted(s1)

        for r in range(k, len(s2) + 1):
            while r - l > k:
                l += 1
            
            if s1 == sorted(s2[l:r]):
                return True
        
        return False


    
