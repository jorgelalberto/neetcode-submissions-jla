from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

            if len(hashmap) <= 2:
                continue

            for num, cnt in list(hashmap.items()):
                hashmap[num] -= 1
                if hashmap[num]==0:
                    hashmap.pop(num)

        for num in hashmap:
            hashmap[num] = 0
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1

        ans = []
        for num, cnt in hashmap.items():
            if cnt > (len(nums) // 3):
                ans.append(num)

        return ans