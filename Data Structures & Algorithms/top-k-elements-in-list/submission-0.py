class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        res = []

        while k != 0:
            for num, count in counts.items():
                if count == max(counts.values()):
                    res.append(num)
                    del counts[num]
                    break

            k -= 1
            
        return res

            