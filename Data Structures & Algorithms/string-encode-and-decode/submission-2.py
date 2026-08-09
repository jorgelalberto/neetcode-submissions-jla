class Solution:

    def encode(self, strs: List[str]) -> str:
        x = "".join([f"{len(wrd)}${wrd}" for wrd in strs])
        print(x)
        return x

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):
            delimeter = s.find("$", i)
            wrd_len = int(s[i:delimeter])
            ans.append(s[delimeter+1:delimeter+1+wrd_len])
            i = delimeter+1+wrd_len
        return ans