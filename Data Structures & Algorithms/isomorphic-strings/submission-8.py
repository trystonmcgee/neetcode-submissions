class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        table = {}
        for i in range(len(s)):
            if s[i] not in table.keys() and t[i] not in table.values():
                table[s[i]] = t[i]
                
        new_s = ""
        for char in s:
            if char not in table:
                return False
            
            new_s += table[char]
    
        return new_s == t 