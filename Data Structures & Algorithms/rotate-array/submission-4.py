class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums:
            return nums
        
        count = 0
        k = k % len(nums)
        q = deque(nums)

        while count < k:
            temp = q.pop()
            q.appendleft(temp)
            count += 1
        
        nums[:] = list(q)

        