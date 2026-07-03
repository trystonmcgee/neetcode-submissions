class Solution:
    def countSeniors(self, details: List[str]) -> int:
        details[:] = [strng[11:13] for strng in details]
        
        count = 0
        for num in details:
            if int(num) > 60:
                count += 1
            
        return count