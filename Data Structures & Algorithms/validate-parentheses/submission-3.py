class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        
        stack = []

        c_to_o = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char not in c_to_o.keys():
                stack.append(char)
                continue
            
            if stack and c_to_o[char] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack
