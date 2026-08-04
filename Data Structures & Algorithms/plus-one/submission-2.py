class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for dig in digits:
            num += str(dig)
        
        num = int(num) + 1

        res = []
        for dig in str(num):
            res.append(int(dig))
        
        return res