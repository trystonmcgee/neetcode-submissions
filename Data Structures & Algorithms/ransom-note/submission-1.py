class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = True
        for char in ransomNote:
            if char in magazine:
                magazine = magazine.replace(char, "", 1)
            else:
                res = False
                break
        
        return res