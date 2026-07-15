class Solution:
    def largestGoodInteger(self, num: str) -> str:
        string = "9876543210"
        res = []
        for i in range(len(string)):
            if string[i] * 3 in num:
                res.append(string[i] * 3)
        
        if res:
            return res[0]
        return ""
        

