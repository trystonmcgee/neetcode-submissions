class Solution:
    def mySqrt(self, x: int) -> int:
        def binary_search(left, right):
            mid = (left + right) // 2

            if mid * mid == x or mid * mid < x and (mid + 1) * (mid + 1) > x:
                return mid
            
            elif mid * mid < x:
                return binary_search(mid + 1, right)
            
            elif mid * mid > x:
                return binary_search(left, mid)
        
        return binary_search(0, x)