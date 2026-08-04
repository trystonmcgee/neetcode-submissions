class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def happy(num):
            if num in seen:
                return False
            
            if squared(num) == 1:
                return True
            
            seen.add(num)
            new = squared(num)

            return happy(new)
        
        def squared(num):
            total = 0
            for dig in str(num):
                total += int(dig) ** 2
            return total
        
        return happy(n)