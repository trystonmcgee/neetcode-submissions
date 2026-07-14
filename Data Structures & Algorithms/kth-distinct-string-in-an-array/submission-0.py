from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        distinct = [x for x in arr if counts[x] == 1]
    
        if len(distinct) >= k:
            return distinct[k - 1]
        else:
            return ""