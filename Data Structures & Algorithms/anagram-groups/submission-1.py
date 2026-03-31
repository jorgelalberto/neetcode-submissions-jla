from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for wrd in strs:
            wrd_bucket = [0]*26
            for char in wrd:
                wrd_bucket[ord(char)-ord('a')]+=1
            ans[tuple(wrd_bucket)].append(wrd)

        return list(ans.values())