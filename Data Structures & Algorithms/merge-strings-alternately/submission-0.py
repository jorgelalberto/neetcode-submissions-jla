class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i = 0

        while i < len(word1) and i < len(word2):
            ans.append(word1[i])
            ans.append(word2[i])
            i += 1
        while i < len(word1):
            ans.append(word1[i])
            i += 1
        while i < len(word2):
            ans.append(word2[i])
            i += 1

        return "".join(ans)