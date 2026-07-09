class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = [s[i] for i in range(-1, -(len(s)) - 1, -1)]
        