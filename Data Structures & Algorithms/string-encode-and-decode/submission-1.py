class Solution:

    def encode(self, strs: List[str]) -> str:
        x = "".join([f"{len(wrd)}${wrd}" for wrd in strs])
        print(x)
        return x

    def decode(self, s: str) -> List[str]:
        # "5$Hello5$World"
        ans = []
        i=0
        while i<len(s):
            j = i
            # j = 1 ; s[1] = "$"
            while s[j] != "$":
                j+= 1
            # s[0:1] = int("5") = 5
            wrd_len = int(s[i:j])
            # s[2:7]
            # 5$Hello
            ans.append(s[j+1:(j+1)+wrd_len])
            i=(j+1)+wrd_len
        return ans