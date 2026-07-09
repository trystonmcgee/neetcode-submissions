class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n_to_c= {}
        res = []
        for lst in grid:
            for num in lst:
                if num not in n_to_c:
                    n_to_c[num] = 1
                else:
                    n_to_c[num] += 1
                    if n_to_c[num] == 2:
                        res.append(num)

        for i in range(1, (len(grid)**2) + 1):
            if i not in n_to_c.keys():
                res.append(i)
        
        return res
        
        

        

        

        
