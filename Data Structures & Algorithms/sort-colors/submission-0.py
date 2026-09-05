class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numToCnt = [0, 0, 0]
        numToPrevCnt = [0, 0, 0]

        for num in nums:
            numToCnt[num] += 1
        numToPrevCnt[1] = numToCnt[0]
        numToPrevCnt[2] = numToCnt[0] + numToCnt[1] 

        for num, (cnt, prevCnt) in enumerate(zip(numToCnt, numToPrevCnt)):
            if cnt != 0:
                for i in range(cnt):
                    nums[prevCnt+i] =  num