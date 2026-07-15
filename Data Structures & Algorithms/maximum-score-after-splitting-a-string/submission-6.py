class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        idx = 0
        while idx < len(s) - 1:
            left = s[:idx + 1].count("0")
            right = s[idx + 1:].count("1")
            print(left)
            print(right)
            if left + right > res:
                res = left + right

            idx += 1

        return res