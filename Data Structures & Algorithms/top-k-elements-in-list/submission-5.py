from collections import defaultdict as dd
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq -> num (but before we get this mapping we have to iter 
        # over nums, so get nums first)
        # freq -> num has to ideally should not be a hashmap,
        # bc then retrieval is (at least from what I have understood)
        # O(log(n))
        # better approach is to define an array of len(nums) and each entry
        # can have mutliple entries
        num_to_freq = dd(int)
        freq_to_nums = [[] for _ in range(len(nums)+1)]
        for num in nums:
            num_to_freq[num] += 1
        for num, freq in num_to_freq.items():
            freq_to_nums[freq] += [num]

        ans = []
        for i in reversed(range(len(freq_to_nums))):
            if k == 0:
                break
            len_freq_to_nums = len(freq_to_nums[i])
            if freq_to_nums[i] != []:
                ans += freq_to_nums[i]
                k -= len_freq_to_nums
        return ans
