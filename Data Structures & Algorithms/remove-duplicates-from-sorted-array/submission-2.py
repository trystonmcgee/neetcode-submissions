class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counts = Counter(nums)

        nums[:] = [num for num in counts.keys()]
        return len(nums)