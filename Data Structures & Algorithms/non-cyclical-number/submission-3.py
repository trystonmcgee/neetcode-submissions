class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        squares = {
            "1" : 1,
            "2": 4,
            "3" : 9,
            "4" : 16,
            "5" : 25,
            "6" : 36,
            "7" : 49,
            "8" : 64,
            "9" : 81,
            "0" : 0
        }

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
                total += squares[dig]
            return total
            
        return happy(n)