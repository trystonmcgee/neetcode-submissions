class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        idx = 0
        checking = words[idx]
        res = set()

        while idx <= len(words) - 1:
            for word in words:
                if word in checking and word != checking:
                    res.add(word)

            idx += 1
            if idx <= len(words) - 1:
                checking = words[idx]
        
        return list(res)
