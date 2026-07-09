class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        valid = []
        i = 0
        j = 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                valid.append(t[j])
                i += 1
                j += 1
            else:
                j += 1

        if s == "".join(valid):
            return True
        return False
