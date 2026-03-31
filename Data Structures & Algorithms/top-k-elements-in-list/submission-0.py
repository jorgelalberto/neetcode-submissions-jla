class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        # this is called bucket tactic
        freq_nums = [[] for i in range(len(nums))] #freq_num hashmap, w/freq's as indices
        ret = []

        for num in nums:
            num_freq[num] += 1
        for num, freq in num_freq.items():
            freq_nums[freq-1].append(num)
        
        print(freq_nums)

        i = 0
        for nums in reversed(freq_nums):
            for num in nums:
                if i<k:
                    ret.append(num)
                    i+=1


        return ret