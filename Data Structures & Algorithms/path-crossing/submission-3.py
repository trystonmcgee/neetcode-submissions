class Solution:
    def isPathCrossing(self, path: str) -> bool:
        res = False
        x, y = 0, 0
        paths = [(x, y)]
        direc = {
            "N" : 1,
            "E" : 1,
            "S" : -1,
            "W" : -1
        }

        for char in path:
            if char == "N" or char == "S":
                y += direc[char]
                if (x, y) in paths:
                    res = True
                    break
                else:
                    paths.append((x, y))
                
            elif char == "E" or char == "W":
                x += direc[char]
                if (x, y) in paths:
                    res = True
                    break
                else:
                    paths.append((x, y))
            
            
        print(paths)
            
        return res
        
            