class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_valid_k(piles: List[int], k: int) -> bool:
            i = 0
            h_temp = 0
            while i < len(piles):
                h_temp += piles[i] // k
                h_temp = h_temp+1 if piles[i]%k!=0 else h_temp
                i+=1
            return False if h_temp > h else True

        l = 1
        r = max(piles)
        min_k = r
        while l<=r:
            k = (l+r)//2
            if is_valid_k(piles, k):
                min_k = min(min_k,k)
                r = k-1
            else:
                l = k+1

        return min_k