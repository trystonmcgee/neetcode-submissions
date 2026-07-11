class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        longest = ""
        letters = []
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            for strng in strs:
                letters.append(strng[i])

            if len(set(letters)) < 2:
                longest += letters[0]
            else:
                break
            
            letters.clear()
        
        return longest

