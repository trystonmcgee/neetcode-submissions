class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            biggest = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > biggest:
                    biggest = arr[j]

            arr[i] = biggest 
        
        arr[-1] = -1
        return arr                