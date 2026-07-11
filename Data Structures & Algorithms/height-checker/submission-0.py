class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = [x for x in heights]
        expected.sort()

        res = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                res += 1

        return res

