class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_bucket = [0]*26
        t_bucket = [0]*26

        for char in s:
            s_bucket[ord(char) - ord('a')] += 1
        for char in t:
            t_bucket[ord(char) - ord('a')] += 1

        for s_cnt, t_cnt in zip(s_bucket, t_bucket):
            if s_cnt != t_cnt: return False

        return True