from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(ransomNote)
        res = True
        for char in ransomNote:
            if char in magazine and counts[char] != 0:
                counts[char] -= 1
                magazine = magazine.replace(char, "", 1)
            else:
                res = False
                break
        
        return res
