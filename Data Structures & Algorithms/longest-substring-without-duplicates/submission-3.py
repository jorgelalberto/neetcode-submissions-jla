class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)

        l = 0
        r = 0
        char_to_ind = {}
        max_len = 0
        while r<len(s):
            if s[r] in char_to_ind:
                l = max(char_to_ind[s[r]]+1,l)
                char_to_ind.pop(s[r])
            max_len = max(max_len, r-l+1)
            char_to_ind[s[r]] = r
            r += 1
        return max_len