class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        count = 0

        while count < k:
            temp = nums.pop()
            nums.insert(0, temp)

            count += 1
        