from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # k = prefixSum_i - prefixSum_i-n
        ans = 0
        prefixSum = 0
        prefixSums = defaultdict(int) # prefixSum:count
        prefixSums[0] = 1 # init w/empty case

        for num in nums:
            prefixSum += num
            if prefixSum-k in prefixSums:
                ans += prefixSums[prefixSum-k]
            prefixSums[prefixSum] += 1

        return ans