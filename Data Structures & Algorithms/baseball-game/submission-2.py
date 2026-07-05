class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                new = stack[-1] + stack[-2]
                res += new
                stack.append(new)
            
            elif operations[i] == "D":
                new = stack[-1] * 2
                res += new
                stack.append(new)

            elif operations[i] == "C":
                res -= stack.pop()
            
            else:
                stack.append(int(operations[i]))
                res += int(operations[i])

        return res
            
