from collections import defaultdict as dd

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = dd(int)

        for s_char, t_char in zip(s, t):
            counts[s_char] += 1
            counts[t_char] -= 1

        return sum(abs(count) for count in counts.values()) == 0