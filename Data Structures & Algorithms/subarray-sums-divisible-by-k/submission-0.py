from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # need to map prefixSum%5 : cnt
        # (prefixSum_i % k) - (prefixSum_i-n % k) = 0
        # prefixSum_i%k = prefix_i-n%k
        ans = 0
        prefixSum = 0
        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        for num in nums:
            prefixSum += num
            if prefixSum % k in prefixSums:
                ans += prefixSums[prefixSum % k]
            prefixSums[prefixSum%k] += 1
        return ans