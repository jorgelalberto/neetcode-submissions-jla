from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = defaultdict(int)
        for num in nums:
            num_to_freq[num]+=1

        freq_to_nums = defaultdict(list)
        for num, freq in num_to_freq.items():
            freq_to_nums[freq].append(num)

        ans = []
        for i in range(len(nums),-1, -1):
            if freq_to_nums[i]:
                for num in freq_to_nums[i]:
                    ans.append(num)
                if len(ans)==k: return ans
        return ans