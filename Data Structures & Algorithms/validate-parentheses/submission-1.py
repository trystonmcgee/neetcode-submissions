class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            if char in open.values():
                stack.append(char)
            
            elif char in open.keys():
                if stack and stack[-1] == open[char]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False
            
            

