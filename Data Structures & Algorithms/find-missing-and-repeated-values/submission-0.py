class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n_to_c= {}
        res = []
        missing = []
        for lst in grid:
            for num in lst:
                if num not in n_to_c:
                    n_to_c[num] = 1
                else:
                    n_to_c[num] += 1
                    if n_to_c[num] == 2:
                        res.append(num)
        
        missing = [i + 1 for i in range(len(grid)**2)]
        for num in missing:
            if num not in n_to_c.keys():
                res.append(num)
        
        return res
        

        

        

        
