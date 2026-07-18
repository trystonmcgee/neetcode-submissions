class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counts = Counter(nums)

        nums[:] = [num for num, count in counts.items()]
        return len(nums)