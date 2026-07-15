class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        curr = 0
        res = 0
        for word in words:
            for char in word:
                if char in allowed_set:
                    curr += 1
            
            if curr == len(word):
                res += 1
            
            curr = 0
        
        return res
