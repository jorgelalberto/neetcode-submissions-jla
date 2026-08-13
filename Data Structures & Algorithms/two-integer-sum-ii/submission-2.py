class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        ans = []

        while l<r:
            num_l = numbers[l]
            num_r = numbers[r]
            num_sum = num_l+num_r


            if num_sum < target:
                l+=1
                continue
            elif num_sum > target:
                r-=1
                continue
            return [l+1, r+1]            