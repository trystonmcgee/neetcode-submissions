from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_pairs = len(nums) // 2
        counts = Counter(nums)

        res = True
        for count in counts.values():
            if count % 2 == 0:
                continue
            else:
                res = False
                break

        return res