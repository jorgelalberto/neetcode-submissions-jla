class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_strs = defaultdict(list)
        for string in strs:
            new_string = ""
            for ltr in sorted(string):
                new_string += ltr
            anagram_strs[new_string].append(string)
        return anagram_strs.values() 
