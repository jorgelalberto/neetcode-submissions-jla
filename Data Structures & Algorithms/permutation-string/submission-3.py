from collections import defaultdict as dd
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_to_cnt = dd(int)
        for char in s1:
            s1_char_to_cnt[char] += 1

        l = 0
        r = 0
        temp_char_to_cnt = dd(int)
        while r<len(s2):
            char = s2[r]
            # invalid
            while char in s1_char_to_cnt and temp_char_to_cnt[char] >= s1_char_to_cnt[char]:
                temp_char_to_cnt[s2[l]] -= 1
                l += 1
                continue
            if char not in s1_char_to_cnt:
                temp_char_to_cnt = dd(int)
                l = r+1
                r = l
                continue

            # valid
            temp_char_to_cnt[char] += 1
            if r - l + 1 == len(s1):
                return True

            r += 1
        return False