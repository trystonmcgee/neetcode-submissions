import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        og = s.replace(" ", "")
        og = list(og)
        og = "".join(char for char in og if char not in string.punctuation).lower()

        new = s.replace(" ", "")
        new = list(new)
        new.reverse()
        new = "".join(char for char in new if char not in string.punctuation).lower()

        return og == new