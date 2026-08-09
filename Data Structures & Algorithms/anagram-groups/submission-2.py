from collections import defaultdict as dd

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # wrd -> unique mapping (len 26 arr tracking count for each char)
        # hashmap keyed on unique mapping so anagrams can be group together i.e.
        # unique mapping : wrd
        hashy = dd(list)
        for wrd in strs:
            char_to_cnt = [0]*26
            for char in wrd:
                char_to_cnt[ord(char)-ord('a')] += 1
            hashy[tuple(char_to_cnt)].append(wrd)
        return [wrd_list for wrd_list in hashy.values()]