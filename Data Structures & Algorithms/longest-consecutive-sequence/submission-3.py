class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNum = set(nums)

        ans = 0
        longest = 0
        for i in range(len(nums)):
            cur = nums[i]
            if ((cur-1) in setNum) == False:
                while (cur in setNum) == True:
                    cur += 1
                    longest += 1
                ans = max(ans, longest)
                longest = 0
        return ans

        