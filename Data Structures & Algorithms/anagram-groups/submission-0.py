class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for strng in strs:
            if "".join(sorted(strng)) not in table:
                table["".join(sorted(strng))] = [strng]
            else:
                table["".join(sorted(strng))].append(strng)
        
        return [strng for sorted, strng in table.items()]