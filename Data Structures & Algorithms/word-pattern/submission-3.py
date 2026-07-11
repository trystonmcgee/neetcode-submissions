class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split(" ")):
            return False
        
        ans = True
        res = {}
        idx = 0
        s_lst = s.split(" ")
        curr = s_lst[idx]

        for char in pattern:
            if char not in res and curr in res.values():
                ans = False
                break

            elif char not in res and idx < len(s_lst):
                res[char] = curr
                idx += 1

            elif char in res and res[char] == curr:
                idx += 1

            elif char in res and res[char] != curr:
                ans = False
                break
            
            if idx < len(s_lst):
                curr = s_lst[idx]

        print(res)
        return ans
            
