class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        char_i = ""
        common_prefixes = 0

        while i<len(strs[0]):
            for wrd in strs:
                char_i = strs[0][i]
                if i>=len(wrd) or char_i != wrd[i]:
                    return strs[0][:common_prefixes] 
            i += 1
            common_prefixes += 1

        return strs[0][:common_prefixes]            