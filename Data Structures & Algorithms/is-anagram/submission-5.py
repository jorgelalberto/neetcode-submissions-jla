from collections import defaultdict as dd

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_to_cnt = dd(int)
        t_char_to_cnt = dd(int)
        for s_char in s:
            s_char_to_cnt[s_char] += 1
        for t_char in t:
            t_char_to_cnt[t_char] += 1
        
        if len(s_char_to_cnt) != len(t_char_to_cnt):
            return False

        for s_char in s_char_to_cnt:
            if s_char not in t_char_to_cnt:
                return False
            if s_char_to_cnt[s_char] != t_char_to_cnt[s_char]:
                return False
        return True