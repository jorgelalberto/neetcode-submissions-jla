from collections import defaultdict as dd
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        char_to_cnt = dd(int)
        max_freq = 0
        max_tot = 0
        while r<len(s):
            char_to_cnt[s[r]] += 1
            max_freq = max(max_freq, char_to_cnt[s[r]])

            while (r-l+1) - max_freq > k:
                char_to_cnt[s[l]] -= 1
                l += 1

            max_tot = max(max_tot, r-l+1)
            r += 1
        return max_tot