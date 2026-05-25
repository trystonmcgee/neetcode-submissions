# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        i = 0
        while i < len(pairs):
            j = i
            while j > 0 and pairs[j].key < pairs[j - 1].key:
                    pairs[j], pairs[j - 1] = pairs[j - 1], pairs[j]
                    j -= 1

            res.append(list(pairs))
            i += 1

        return res
