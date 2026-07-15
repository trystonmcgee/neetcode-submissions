class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        paths = {(x,y)}
        direc = {
            "N" : (0, 1),
            "E" : (1, 0),
            "S" : (0, -1),
            "W" : (-1, 0)
        }
        
        for char in path:
            dx, dy = direc[char]
            x += dx
            y += dy
        
            if (x, y) in paths:
                return True
            paths.add((x, y)) 

        return False
