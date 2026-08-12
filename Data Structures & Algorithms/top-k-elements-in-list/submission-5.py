class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums -> min heap (count, value)
        # Ex 1. min heap -> [(1, 1), (2, 2), (3, 3)] len(minheap) > k
        # While len > k, remove first element

        # Edge Cases: empty list

        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)

        if not nums:
            return nums
        
        counts = Counter(nums)
        min_heap = []

        for num, count in counts.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for count, num in min_heap]