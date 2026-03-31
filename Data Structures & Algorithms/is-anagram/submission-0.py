from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s += "abcdefghijklmnopqrstuvwxyz"
        t += "abcdefghijklmnopqrstuvwxyz"
        hashy_s = defaultdict(int)
        hashy_t = defaultdict(int)

        for ltr in s:
            hashy_s[ltr] += 1
        for ltr in t:
            hashy_t[ltr] += 1

        for key, val_s in hashy_s.items():
            if hashy_t[key] != val_s:
                return False
        
        return True
        
